from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from typing import Optional
import boto3

app = FastAPI()

# AWS Polly client setup
polly_client = boto3.client('polly')

# mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# serve the landing page
@app.get("/")
def read_root():
    return FileResponse('static/index.html')

# post route to generate test
@app.post('/generate-test')
async def generate_test(request: Request):
    body = await request.json()
    code_block = body.get('code', '')
    if not code_block:
        raise HTTPException(status_code = 400, detail = 'No code block provided')
    else:
        print(code_block)

    # placeholder for logic to generate test using LLM
    generated_test = "def test_function():\n    assert True  # Placeholder for generated test"

    # placeholder for logic to get explanation from LLM
    explanation = "This test checks if the function always returns True, which is a basic example."

    return JSONResponse(content={"test": generated_test, 'explanation': explanation})


@app.post("/generate-audio")
async def generate_audio(request: Request):
    body = await request.json()
    text = body.get("text", "")
    lang = body.get("lang", "en-US")  # default to US English for testing but this will come from the front end

    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    try:
        response = polly_client.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId='Joanna',  # hardcoded voice, as a nice to have, we can make this selectable by the user
            LanguageCode=lang
        )
        
        # stream the audio back to the client
        return StreamingResponse(response['AudioStream'], media_type="audio/mp3")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from typing import Optional

app = FastAPI()

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

    return JSONResponse(content={"test": generated_test})
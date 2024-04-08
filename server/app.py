from chalice import Chalice, Response
from services.audioservice import AudioService
from services.testgenerationservice import TestGenerationService
import os

app = Chalice(app_name='server')
audioservice = AudioService()
testgenerationservice = TestGenerationService()

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/generate-test', methods=['POST'])
def generate_test():
    request = app.current_request
    body = request.json_body
    code_block = body.get('code', '')
    if not code_block:
        return Response(body='No code block provided', status_code=400)
    else:
        print(code_block)

    generated_test = testgenerationservice.generate_test(code_block)

    return {'test': generated_test['test'], 'explanation': generated_test['explanation']}

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    request = app.current_request
    body = request.json_body
    text = body.get("text", "")
    target_lang = body.get("lang", "en-US")
    
    audio = audioservice.generate_audio(text, target_lang)

    return Response(body=audio, headers={'Content-Type': 'audio/mpeg'}, status_code=200)
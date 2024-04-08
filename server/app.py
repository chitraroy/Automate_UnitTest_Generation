from chalice import Chalice, Response
import os

app = Chalice(app_name='server')


@app.route('/')
def index():
    # Define the path to your HTML file
    html_file_path =  'static/index.html'
    
    # Read the content of the HTML file
    with open(html_file_path, 'r') as html_file:
        html_content = html_file.read()
    
    # Return the HTML content with the correct content-type header
    return Response(body=html_content,
                        status_code=200,
                        headers={'Content-Type': 'text/html'})

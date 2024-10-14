from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Set up the directory where the website files will be served from
website_directory = ''

@app.route('/')
def serve_index():
    return send_from_directory(website_directory, 'index.html')

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(website_directory, filename)

def run_server(folder):
    global website_directory
    website_directory = folder
    app.run(host='0.0.0.0', port=80)

if __name__ == "__main__":
    import sys
    folder = sys.argv[1]  # Folder passed as an argument from GUI
    run_server(folder)

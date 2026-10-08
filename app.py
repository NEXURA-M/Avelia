import os
import sys
import webbrowser
from threading import Timer
from flask import Flask, send_from_directory

if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/<path:filename>')
def serve_files(filename):
    return send_from_directory(BASE_DIR, filename)

def open_browser():
    # Yahan humne address ko sahi kar ke 127.0.0.1 kiya hai
    webbrowser.open("http://127.0.0")

if __name__ == '__main__':
    Timer(1.5, open_browser).start()
    # Yahan host="127.0.0.1" likhna zaroori hai taake local system par hi chale
    app.run(host="127.0.0.0", port=5000, debug=False)

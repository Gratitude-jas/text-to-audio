from flask import Flask, request, render_template_string
from gtts import gTTS
import subprocess
import platform

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template_string(open("index.html").read())

@app.route('/speak', methods=['POST'])
def speak():
    try:
        text = request.form['text']
        tts = gTTS(text=text, lang='en')
        tts.save("speech.mp3")

        system_name = platform.system()
        if system_name == "Windows":
            subprocess.run(["start", "speech.mp3"], shell=True)
        elif system_name == "Darwin":
            subprocess.run(["afplay", "speech.mp3"])
        else:
            subprocess.run(["mpg321", "speech.mp3"])
            
        return "✅ Speech played successfully! <a href='/'>Back</a>"
    except Exception as e:
        return f"<p style='color:red;'>⚠️ Error: {e}</p><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(debug=True)

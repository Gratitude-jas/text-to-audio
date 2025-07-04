from gtts import gTTS
import subprocess
import platform

# Enter the text you want to convert to speech
text = input("Enter text to speak: ")

# Convert the text to speech
tts = gTTS(text=text, lang='en')

# Save the audio file
tts.save("speech.mp3")

# Play the saved audio file using system player
system_name = platform.system()
if system_name == "Windows":
    subprocess.run(["start", "speech.mp3"], shell=True)
elif system_name == "Darwin":  # macOS
    subprocess.run(["afplay", "speech.mp3"])
else:  # Linux
    subprocess.run(["mpg321", "speech.mp3"])

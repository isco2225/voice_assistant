from gtts import gTTS
import playsound
import uuid
import os

def speak_with_gtts(text: str):
    filename = f"temp_{uuid.uuid4()}.mp3"
    try:
        tts = gTTS(text=text, lang='tr')
        tts.save(filename)
        playsound.playsound(filename)
    finally:
        if os.path.exists(filename):
            os.remove(filename)

from gtts import gTTS
import playsound
import os
import uuid

def speak(text):
    filename = f"temp_{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang='tr')
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)




#import pyttsx3

#engine = pyttsx3.init()
#engine.setProperty('rate', 150)
#engine.setProperty('volume', 0.9)

#def speak(text):
#    engine.say(text)
#    engine.runAndWait()
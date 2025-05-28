import pyttsx3

_engine = pyttsx3.init()
_engine.setProperty('rate', 150)
_engine.setProperty('volume', 0.9)

def speak_with_pyttsx3(text: str):
    _engine.say(text)
    _engine.runAndWait()

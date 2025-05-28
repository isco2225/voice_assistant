from utils.network_check import has_internet_connection
from core.output.synthesizer_gtts import speak_with_gtts
from core.output.synthesizer_pyttsx3 import speak_with_pyttsx3

def speak(text: str):
    if has_internet_connection():
        try:
            speak_with_gtts(text)
        except Exception as e:
            print(f"⚠️ gTTS başarısız: {e}, offline moda geçiliyor.")
            speak_with_pyttsx3(text)
    else:
        speak_with_pyttsx3(text)

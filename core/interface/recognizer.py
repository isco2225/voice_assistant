from utils.network_check import has_internet_connection
from core.input.recognizer_google import recognize_with_google
from core.input.recognizer_vosk import recognize_with_vosk

def recognize_speech():
    if has_internet_connection():
        return recognize_with_google()
    else:
        return recognize_with_vosk()
    

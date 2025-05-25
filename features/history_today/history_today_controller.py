from features.history_today.history_today_service import fetch_today_event
from utils.translator import translate_to_turkish
from core.synthesizer import speak

def tell_today_in_history():
    speak("Bugün tarihte ne olmuş bir bakalım...")
    year, text = fetch_today_event()
    
    if text:
        translated = translate_to_turkish(text)
        message = f"{year} yılında bugün, {translated}"
        speak(message)
        print(f"📜 {message}")
    else:
        speak("Tarihte bugün ne olduğunu öğrenemedim.")

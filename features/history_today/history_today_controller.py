from features.history_today.history_today_service import fetch_today_event
from utils.translator import translate_to_turkish
from core.interface.synthesizer import speak

def tell_today_in_history():
    speak("Bugün tarihte ne olmuş bir bakalım...")

    year, text = fetch_today_event()
    if not text:
        speak("Tarihte bugün ne olduğunu öğrenemedim.")
        return

    translated = translate_to_turkish(text)

    if translated:
        message = f"{year} yılında bugün, {translated}"
    else:
        speak("Çeviri başarısız oldu. Orijinal metni okuyorum.")
        message = f"{year} yılında bugün, {text}"

    speak(message)
    print(f"{message}")

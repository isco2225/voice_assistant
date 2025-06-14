import webbrowser
from core.interface.synthesizer import speak
from features.space_information.space_information_service import fetch_space_info
from utils.translator import translate_to_turkish

def give_space_info():
    speak("Bugünün uzay bilgisini getiriyorum...")
    data = fetch_space_info()

    if not data:
        speak("Veriye şu anda ulaşamıyorum.")
        return

    title_tr = translate_to_turkish(data["title"])
    explanation_tr = translate_to_turkish(data["explanation"])

    try:
        webbrowser.open(data["url"])
    except Exception as e:
        print(f"Tarayıcıda açma hatası: {e}")

    speak(f"Başlık: {title_tr}")
    speak(explanation_tr)
    print(f"URL: {data['url']}")
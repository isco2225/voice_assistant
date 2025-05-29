from core.interface.synthesizer import speak
from core.interface.recognizer import recognize_speech
from features.wikipedia.wikipedia_service import fetch_wikipedia_summary

def search_wikipedia():
    speak("Ne hakkında araştırma yapmamı istersiniz?")
    try:
        topic = recognize_speech()
    except Exception:
        speak("Sizi anlayamadım.")
        return

    if topic:
        speak(f"{topic} hakkında araştırıyorum...")
        summary = fetch_wikipedia_summary(topic)
        speak(summary)
        print(f"📚 Wikipedia: {summary}")
    else:
        speak("Hiçbir konu algılayamadım.")

from core.synthesizer import speak
from features.facts.facts_service import fetch_random_fact
from utils.translator import translate_to_turkish


def give_fact():
    speak("Bir bilgi getiriyorum...")
    fact = fetch_random_fact()

    if fact:
        translated_fact = translate_to_turkish(fact)
        speak(f"{translated_fact}")
        print(f"📚 Bilgi: {translated_fact}")
    else:
        speak("Bilgiye şu anda ulaşamıyorum.")

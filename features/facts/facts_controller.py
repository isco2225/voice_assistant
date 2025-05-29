from core.interface.synthesizer import speak
from features.facts.facts_service import fetch_random_fact
from utils.translator import translate_to_turkish

def give_fact():
    speak("Bir bilgi getiriyorum...")
    fact = fetch_random_fact()
    if not fact:
        speak("Bilgiye şu anda ulaşamıyorum.")
        return
    translated_fact = translate_to_turkish(fact)
    if translated_fact:
        speak(translated_fact)
        print(f"📚 Bilgi (TR): {translated_fact}")
    else:
        speak("Bilgiyi çeviremedim ama orijinalini okuyorum.")
        speak(fact)
        print(f"📚 Orijinal Bilgi (EN): {fact}")

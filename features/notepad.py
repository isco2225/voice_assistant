import datetime
from core import recognizer, synthesizer

def take_note():
    synthesizer.speak("Ne not almak istersiniz?")
    note = recognizer.recognize_speech()

    if note in ["anlaşılamadı", "bağlantı hatası"]:
        synthesizer.speak("Sizi anlayamadım.")
        return

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {note}\n")

    synthesizer.speak("Not kaydedildi.")

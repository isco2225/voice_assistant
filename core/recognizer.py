import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinleniyor...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="tr-TR")
        print("Algılanan:", text)
        return text.lower()
    except sr.UnknownValueError:
        return "anlaşılamadı"
    except sr.RequestError:
        return "bağlantı hatası"

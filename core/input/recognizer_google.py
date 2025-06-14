import speech_recognition as sr
from config.config import RECOGNITION_LANGUAGE, RECOGNITION_TIMEOUT, RECOGNITION_PHRASE_TIMEOUT
from core.exceptions import RecognitionError

def recognize_with_google():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(
                source,
                timeout=None,
                phrase_time_limit=RECOGNITION_PHRASE_TIMEOUT
            )
        except sr.WaitTimeoutError:
            raise RecognitionError("Konuşma algılanamadı (timeout).")

    try:
        return recognizer.recognize_google(audio, language=RECOGNITION_LANGUAGE).lower()
    except sr.UnknownValueError:
        raise RecognitionError("Ses anlaşılamadı.")
    except sr.RequestError as e:
        raise RecognitionError(f"internet bağlantınızı kontrol ediniz.")

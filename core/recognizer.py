import speech_recognition as sr
from config.settings import RECOGNITION_LANGUAGE, RECOGNITION_TIMEOUT, RECOGNITION_PHRASE_TIMEOUT
from utils.logger import logger
from utils.exceptions import RecognitionError

def recognize_speech():
    """
    Recognize speech from microphone input
    
    Returns:
        str: Recognized text in lowercase
        
    Raises:
        RecognitionError: If speech recognition fails
    """
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 4000
    recognizer.dynamic_energy_threshold = True
    
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(
                source,
                timeout=RECOGNITION_TIMEOUT,
                phrase_time_limit=RECOGNITION_PHRASE_TIMEOUT
            )
        except sr.WaitTimeoutError:
            raise RecognitionError("Ses algılanamadı")
        except Exception as e:
            raise RecognitionError(f"Mikrofon hatası: {str(e)}")

    try:
        text = recognizer.recognize_google(audio, language=RECOGNITION_LANGUAGE)
        return text.lower()
    except sr.UnknownValueError:
        raise RecognitionError("Ses anlaşılamadı")
    except sr.RequestError as e:
        raise RecognitionError(f"Google Speech API hatası: {str(e)}")

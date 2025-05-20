import datetime
import os
from core import recognizer, synthesizer
from utils.logger import logger
from utils.exceptions import RecognitionError

def take_note():
    try:
        synthesizer.speak("Ne not almak istersiniz?")
        note = recognizer.recognize_speech()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("notes.txt", "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {note}\n")
        
        logger.info(f"Note saved: {note}")
        synthesizer.speak("Not kaydedildi.")
        
    except RecognitionError as e:
        logger.error(f"Failed to recognize note: {str(e)}")
        synthesizer.speak("Sizi anlayamadım.")
    except IOError as e:
        logger.error(f"Failed to save note: {str(e)}")
        synthesizer.speak("Not kaydedilirken bir hata oluştu.")
    except Exception as e:
        logger.error(f"Unexpected error while taking note: {str(e)}")
        synthesizer.speak("Beklenmeyen bir hata oluştu.")

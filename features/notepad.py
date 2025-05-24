import datetime
import os
from core import recognizer, synthesizer
from utils.logger import logger
from utils.exceptions import RecognitionError

def take_note():
    """
    Take a voice note and save it to notes.txt
    
    The note will be saved with a timestamp in the format:
    [YYYY-MM-DD HH:MM:SS] Note content
    """
    try:
        synthesizer.speak("Ne not almak istersiniz?")
        note = recognizer.recognize_speech()

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("notes.txt", "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {note}\n")
        
        synthesizer.speak("Not kaydedildi.")
        
    except RecognitionError as e:
        logger.debug(f"Note recognition failed: {str(e)}")
        return
    except IOError as e:
        logger.error(f"Failed to save note: {str(e)}")
        return
    except Exception as e:
        logger.error(f"Unexpected error while taking note: {str(e)}")
        return

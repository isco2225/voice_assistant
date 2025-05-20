import pyttsx3
from utils.logger import logger
from utils.exceptions import SynthesisError
from config.settings import SYNTHESIS_LANGUAGE, SYNTHESIS_RATE, SYNTHESIS_VOLUME

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Configure the engine
engine.setProperty('rate', SYNTHESIS_RATE)
engine.setProperty('volume', SYNTHESIS_VOLUME)

# Set the voice
voices = engine.getProperty('voices')
for voice in voices:
    if SYNTHESIS_LANGUAGE in voice.id:
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    """
    Convert text to speech and speak it out loud
    
    Args:
        text (str): The text to be spoken
        
    Raises:
        SynthesisError: If speech synthesis fails
    """
    try:
        logger.debug(f"Speaking: {text}")
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        logger.error(f"Speech synthesis error: {str(e)}")
        raise SynthesisError(f"Speech synthesis failed: {str(e)}")

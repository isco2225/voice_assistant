from core import recognizer, synthesizer, commands
from utils.logger import logger
from utils.exceptions import RecognitionError, SynthesisError, CommandError
from config.settings import EXIT_COMMANDS

def main():
    try:
        logger.info("Voice Assistant başlatılıyor...")        
        while True:
            try:
                command = recognizer.recognize_speech()
                logger.debug(f"Algılanan komut: {command}")
                if command.lower() in EXIT_COMMANDS:
                    logger.info("Çıkış komutu algılandı")
                    synthesizer.speak("Görüşmek üzere.")
                    break
                commands.handle_command(command)
            except RecognitionError as e:
                logger.error(f"Ses tanıma hatası: {str(e)}")
                synthesizer.speak("Üzgünüm, sizi anlayamadım.")
            except CommandError as e:
                logger.error(f"Komut işleme hatası: {str(e)}")
                synthesizer.speak("Bu komutu işleyemedim.")
    except Exception as e:
        logger.critical(f"Beklenmeyen hata: {str(e)}")
        raise
    finally:
        logger.info("Voice Assistant kapatılıyor...")
if __name__ == "__main__":
    main()

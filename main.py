from core.interface.recognizer import recognize_speech
from core.exceptions import RecognitionError
from features.welcome.welcome import handle_welcome
from router.command_router import handle_command
from utils.printer import systemPrint, customPrint, Emojis

def main():
    systemPrint("Sesli Asistan başlatılıyor...")
    handle_welcome()
    while True:
        try:
            customPrint(Emojis.MICROPHONE, "Dinleme başladı...")
            text = recognize_speech()
            if text:
                customPrint(Emojis.MATCH, f"Algılanan komut: {text}")
                handle_command(text)
        except RecognitionError as e:
            print(str(e))

if __name__ == "__main__":
    main()

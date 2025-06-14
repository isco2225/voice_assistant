from core.interface.recognizer import recognize_speech
from core.exceptions import RecognitionError
from features.welcome.welcome import handle_welcome
from router.command_router import handle_command
from utils.printer import Colors, customPrint

def main():
    customPrint("Sesli Asistan başlatılıyor...")
    #handle_welcome()
    while True:
        try:
            customPrint("Dinleme başladı...",color= Colors.BLUE)
            text = recognize_speech()
            if text:
                customPrint(f"Algılanan komut: {text}")
                handle_command(text)
        except RecognitionError as e:
            print(str(e))

if __name__ == "__main__":
    main()

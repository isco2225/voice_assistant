from core.interface.recognizer import recognize_speech
from core.interface.synthesizer import speak
from core.exceptions import RecognitionError
from features.welcome.welcome import handle_welcome
from router.command_router import handle_command

def main():
    handle_welcome(15)
    while True:
        try:
            print('dinleme başladı...')
            text = recognize_speech()
            if text:
                print('Komut: '+text)
                handle_command(text)
        except RecognitionError as e:
            speak(str(e))

if __name__ == "__main__":
    main()

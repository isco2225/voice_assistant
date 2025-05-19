from core import recognizer, synthesizer, commands

def main():
    synthesizer.speak("Nasıl yardımcı olabilirim?")
    while True:
        command = recognizer.recognize_speech()
        if command in ["çık", "kapat"]:
            synthesizer.speak("Görüşmek üzere.")
            break
        commands.handle_command(command)

if __name__ == "__main__":
    main()

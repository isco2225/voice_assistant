from core.listener import listen
from core.synthesizer import speak
from router.command_router import handle_command
import time
import winsound
from config.config import BEEP_FREQUENCY, BEEP_DURATION


def play_beep():
    winsound.Beep(BEEP_FREQUENCY, BEEP_DURATION)

def main():
    print("🎙️ Voice Assistant başlatıldı. Dinlemeye geçiliyor...")
    speak("Voice assistant başlatıldı. Ne yapmamı istersiniz.")

    while True:
        print("🎤 Dinleme başlıyor...")
        play_beep()
        text = listen()

        if text:
            print(f"🗣️ Komut: {text}")
            handle_command(text)
        else:
            print("🔇 Sessizlik veya anlaşılmayan ses algılandı, dinlemeye devam ediliyor...")

        time.sleep(0.5)

if __name__ == "__main__":
    main()

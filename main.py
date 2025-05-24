from core.listener import listen
from core.synthesizer import speak
from features.open_app.open_app import handle_command
import time


def main():
    print("🎙️ Voice Assistant başlatıldı. Dinlemeye geçiliyor...")
    speak("Voice assistant başlatıldı. Konuşabilirsiniz.")

    while True:
        print("🎤 Dinleme başlıyor...")
        text = listen()
        
        if text:
            print(f"🗣️ Komut: {text}")
            handle_command(text)
        else:
            print("🔇 Sessizlik veya anlaşılmayan ses algılandı, dinlemeye devam ediliyor...")
        time.sleep(0.5)  # kısa bekleme
if __name__ == "__main__":
    main()

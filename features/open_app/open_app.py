import os
import webbrowser
from core.synthesizer import speak
from features.time_query.time_query import handle_time_command, handle_date_command
import winsound

def play_beep():
    frequency = 1000  # Hertz
    duration = 300    # milliseconds
    winsound.Beep(frequency, duration)

def open_website(url, name):
    speak(f"{name} açılıyor.")
    webbrowser.open(url)
    play_beep()

def open_application(path, name):
    speak(f"{name} açılıyor.")
    try:
        os.startfile(path)
        play_beep()
    except FileNotFoundError:
        speak(f"{name} bulunamadı.")




def handle_command(text):
    text = text.lower()

    if any(keyword in text for keyword in ["tarayıcıyı aç", "google'ı aç"]):
        open_website("https://www.google.com", "Tarayıcı")

    elif any(keyword in text for keyword in ["youtube'u aç", "youtube aç"]):
        open_website("https://www.youtube.com", "YouTube")

    elif any(keyword in text for keyword in ["geliştirici modu", "yazılımcı modu", "vs code'u aç"]):
        open_application(
            r"C:\Users\omran\AppData\Local\Programs\Microsoft VS Code\Code.exe",
            "Visual Studio Code"
        )

    elif any(keyword in text for keyword in ["spotify'ı aç", "spotify aç"]):
        open_application(
            r"C:\Users\omran\AppData\Roaming\Spotify\Spotify.exe",
            "Spotify"
        )

    elif any(keyword in text for keyword in ["saat kaç", "kaç saat", "saat nedir"]):
        handle_time_command()

    elif any(keyword in text for keyword in ["tarih", "bugünün tarihi", "bugün ne gün"]):
        handle_date_command()


    else:
        speak("Bu komutu anlayamadım.")
        print(f"❓ Anlaşılamayan komut: {text}")

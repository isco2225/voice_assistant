from utils.launcher import launch
from core.synthesizer import speak

def open_developer_mode():
    speak("Geliştirici modu başlatılıyor. Lütfen bekleyin.")

    apps_to_launch = [
        {
            "path": r"C:\Program Files\Docker\Docker Desktop.exe",
            "name": "Docker Desktop"
        },
        {
            "path": r"C:\Users\omran\AppData\Local\Programs\Microsoft VS Code\Code.exe",
            "name": "Visual Studio Code"
        },
        {
            "path": r"C:\Program Files\Beekeeper Studio\beekeeper-studio.exe",
            "name": "Beekeeper Studio"
        }
    ]

    for app in apps_to_launch:
        launch(app["path"], app["name"])

    speak("Tüm geliştirici araçları başlatıldı.")

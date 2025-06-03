from utils.launcher import launch
from core.interface.synthesizer import speak

def open_developer_mode():
    speak("Geliştirici modu başlatılıyor. Lütfen bekleyin.")

    apps_to_launch = [
        {
            "path": r"C:\ProgramData\Microsoft\Windows\Start Menu\Docker Desktop.lnk",
            "name": "Docker Desktop"
        },
        {
            "path": r"C:\Users\omran\AppData\Local\Programs\Microsoft VS Code\Code.exe",
            "name": "Visual Studio Code"
        },
        {
            "path": r"C:\Users\omran\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Beekeeper Studio.lnk",
            "name": "Beekeeper Studio"
        }
    ]

    for app in apps_to_launch:
        launch(app["path"], app["name"])
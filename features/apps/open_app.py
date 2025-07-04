from utils.launcher import launch

def open_application(app_key):
    apps = {
        "spotify": (r"C:\Users\omran\AppData\Local\Microsoft\WindowsApps\Spotify.exe", "Spotify"),
        "vs_code": (r"C:\Users\omran\AppData\Local\Programs\Microsoft VS Code\bin\code", "Visual Studio Code")
    }

    if app_key in apps:
        path, name = apps[app_key]
        launch(path, name) 

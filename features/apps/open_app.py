from utils.launcher import launch

def open_application(app_key):
    apps = {
        "spotify": (r"C:\...\Spotify.exe", "Spotify"),
        "vs_code": (r"C:\...\Code.exe", "Visual Studio Code")
    }

    if app_key in apps:
        path, name = apps[app_key]
        launch(path, name)  # 👈 is_web=False varsayılan zaten

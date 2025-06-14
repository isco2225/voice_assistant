import os
import webbrowser
from core.interface.synthesizer import speak
from utils.information_sound import play_beep

def launch(target: str, name: str, is_web: bool = False):
    speak(f"{name} açılıyor.")
    try:
        if is_web:
            webbrowser.open(target)
        else:
            os.startfile(target)
        play_beep()
    except FileNotFoundError:
        speak(f"{name} bulunamadı.")
    except Exception as e:
        speak(f"{name} açılırken bir hata oluştu.")
        print(f"Başlatma hatası ({name}): {e}")

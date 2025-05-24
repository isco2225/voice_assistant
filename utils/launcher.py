import os
import webbrowser
import winsound
from core.synthesizer import speak

def play_beep():
    winsound.Beep(1000, 300)

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
        print(f"🔥 Başlatma hatası ({name}): {e}")

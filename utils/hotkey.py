import keyboard
import threading

def register_hotkey(on_trigger):
    def listen_hotkey():
        print("⌨️ [hotkey] ctrl+ş kombinasyonu dinleniyor...")
        while True:
            keyboard.wait('ctrl+ş')
            print("✅ [hotkey] ctrl+ş algılandı. handle_trigger çağrılıyor...")
            on_trigger()

    thread = threading.Thread(target=listen_hotkey, daemon=True)
    thread.start()

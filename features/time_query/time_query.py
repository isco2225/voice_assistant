from datetime import datetime
from core.synthesizer import speak

def handle_time_command():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    speak(f"Şu an saat {current_time}")
    print(f"🕒 Saat bilgisi verildi: {current_time}")

def handle_date_command():
    now = datetime.now()
    current_date = now.strftime("%d %B %Y")
    speak(f"Şu an tarih {current_date}")
    print(f"📅 Tarih bilgisi verildi: {current_date}")


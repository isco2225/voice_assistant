from datetime import datetime
from core.interface.synthesizer import speak
from features.exchange_rate.exchange_rate_service import fetch_exchange_data
from features.weather.weather_controller import give_weather_advice
from utils.network_check import has_internet_connection

def handle_morning_greeting():
    speak("Günaydın. Güncel döviz kuru bilgileri getiriliyor.")

    exchange_data = fetch_exchange_data()

    if not exchange_data:
        speak("Döviz bilgilerine şu anda ulaşılamıyor.")
        return

    usd = exchange_data["usd"]
    eur = exchange_data["eur"]

    message = f"Bir Amerikan doları {usd:.1f} Türk lirası, bir Euro ise {eur:.1f} Türk lirası."
    speak(message)
    print(f"📢 {message}")

def handle_evening_greeting():
    speak("İyi akşamlar.")
    give_weather_advice()

def handle_welcome(hour: int):
    if not has_internet_connection():
        speak("Selam, Kaliteli bir hizmet alabilmek için internete bağlanın")
        return
        
    #now = datetime.now()
    #hour = now.hour

    if 9 <= hour < 13:
        handle_morning_greeting()
    elif 13 <= hour < 23:
        handle_evening_greeting()
    else:
        speak("Selam, bu saatte uyuman lazımdı.Nasıl yardımcı olabilirim.")

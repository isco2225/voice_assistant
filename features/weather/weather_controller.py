from core.interface.synthesizer import speak
from features.weather.weather_service import fetch_current_weather
from features.weather.weather_utils import describe_weather_code, generate_weather_advice

def give_weather_advice():
    speak("Hava durumu bilgisi getiriliyor...")

    weather = fetch_current_weather()

    if not weather:
        speak("Hava durumu bilgisine şu anda ulaşılamıyor.")
        return

    temperature = weather["temperature"]
    windspeed = weather["windspeed"]
    code = weather["weather_code"]

    condition = describe_weather_code(code)
    advice = generate_weather_advice(temperature)

    message = (
        f"Şu anda İstanbul'da hava {condition}, {temperature} derece,"
        f"rüzgar ise {windspeed} kilometre hızında."
    )

    speak(message + advice)

    print(f"🌤 {message}")
    print(f"🧥 Tavsiye: {advice}")

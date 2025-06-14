from core.interface.synthesizer import speak
from features.exchange_rate.exchange_rate_service import fetch_exchange_data

def tell_exchange_rate():
    speak("Güncel döviz kuru bilgileri getiriliyor...")

    exchange_data = fetch_exchange_data()

    if not exchange_data:
        speak("Döviz bilgilerine şu anda ulaşılamıyor.")
        return

    usd = exchange_data["usd"]
    eur = exchange_data["eur"]

    message = (
        f"1 Amerikan doları {usd:.1f} Türk lirası, "
        f"1 Euro ise {eur:.1f} Türk lirası."
    )

    speak(message)
    print(f"{message}")

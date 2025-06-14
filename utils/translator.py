import requests
from config.config import TRANSLATE_API_URL

def translate_to_turkish(text):
    try:
        response = requests.get(TRANSLATE_API_URL, params={"dl": "tr", "text": text}, timeout=10)
        response.raise_for_status()
        data = response.json()
        translated = data.get("destination-text")
        if translated:
            return translated
        else:
            print("API yanıtında çeviri bulunamadı.")
            return None
    except requests.Timeout:
        print("Çeviri API zaman aşımına uğradı.")
    except requests.RequestException as e:
        print(f"Çeviri isteği hatası: {e}")
    except Exception as e:
        print(f"Beklenmeyen çeviri hatası: {e}")
    return None 
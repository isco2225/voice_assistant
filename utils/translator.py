import requests
from config.config import TRANSLATE_API_URL

def translate_to_turkish(text):
    url = TRANSLATE_API_URL
    params = {
        "dl": "tr",
        "text": text
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("destination-text", text)
        else:
            print(f"Çeviri hatası: {response.status_code}")
            print(f"Çeviri hatası: {response.text}")
            return text
    except requests.RequestException as e:
        print(f"İstek hatası: {e}")
        return text

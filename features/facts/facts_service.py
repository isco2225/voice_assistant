import requests
from config.config import FACTS_API_URL

def fetch_random_fact():
    try:
        response = requests.get(FACTS_API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        text = data.get("text")

        if text:
            return text
        else:
            print("API yanıtında 'text' bulunamadı.")
            return None
    except requests.Timeout:
        print("⏱️ İstek zaman aşımına uğradı.")
    except requests.RequestException as e:
        print(f"🌐 İstek hatası: {e}")
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")

    return None

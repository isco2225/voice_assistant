import requests
from config.config import NASA_API_URL, NASA_API_KEY

def fetch_space_info():
    try:
        response = requests.get(f"{NASA_API_URL}?api_key={NASA_API_KEY}", timeout=5)
        response.raise_for_status()
        data = response.json()

        title = data.get("title")
        explanation = data.get("explanation")
        url = data.get("url")

        if title and explanation and url:
            return {
                "title": title,
                "explanation": explanation,
                "url": url
            }
        else:
            print("⚠️ Beklenen veri alanları eksik.")
            return None

    except requests.Timeout:
        print("⏱️ NASA API isteği zaman aşımına uğradı.")
    except requests.RequestException as e:
        print(f"🌐 İstek hatası: {e}")
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")

    return None

import requests
from config.config import HISTORY_TODAY_API_URL

def fetch_today_event():
    try:
        response = requests.get(HISTORY_TODAY_API_URL, timeout=5)
        response.raise_for_status()

        data = response.json()
        events = data.get("data", {}).get("Events", [])

        if events:
            event = events[0]
            year = event.get("year")
            text = event.get("text")

            if year and text:
                return year, text
            else:
                print("Etkinlik verisi eksik.")
        else:
            print("Etkinlik listesi boş.")

    except requests.Timeout:
        print("⏱️ İstek zaman aşımına uğradı.")
    except requests.RequestException as e:
        print(f"🌐 İstek hatası: {e}")
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")

    return None, None

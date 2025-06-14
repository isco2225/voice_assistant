import requests

from config.config import EXCHANGE_RATE_API_URL

def fetch_exchange_data():
    url = EXCHANGE_RATE_API_URL
    try:
        response = requests.get(url, timeout=8)
        response.raise_for_status()
        data = response.json()

        usd = data.get("USDTRY", {}).get("bid")
        eur = data.get("EURTRY", {}).get("bid")

        if usd and eur:
            return {
                "usd": float(usd),
                "eur": float(eur)
            }
        else:
            print("Kur verilerinden bazıları eksik.")
            return None

    except requests.Timeout:
        print("Döviz API isteği zaman aşımına uğradı.")
    except requests.RequestException as e:
        print(f"Döviz API bağlantı hatası: {e}")
    except Exception as e:
        print(f"Beklenmeyen döviz servisi hatası: {e}")

    return None

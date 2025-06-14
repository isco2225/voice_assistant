import requests

def fetch_current_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=41.01&longitude=28.97&current_weather=true"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        current = data.get("current_weather", {})
        temperature = current.get("temperature")
        windspeed = current.get("windspeed")
        weather_code = current.get("weathercode")

        if temperature is not None:
            return {
                "temperature": temperature,
                "windspeed": windspeed,
                "weather_code": weather_code
            }
        else:
            print("Hava durumu verisi eksik.")
            return None

    except requests.Timeout:
        print("Hava durumu isteği zaman aşımına uğradı.")
    except requests.RequestException as e:
        print(f"Hava durumu API hatası: {e}")
    except Exception as e:
        print(f"Beklenmeyen hava durumu hatası: {e}")

    return None

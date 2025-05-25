import requests

def fetch_today_event():
    try:
        response = requests.get("https://history.muffinlabs.com/date", timeout=5)
        if response.status_code == 200:
            data = response.json()
            events = data["data"]["Events"]
            if events:
                return events[0]["year"], events[0]["text"]  # İlk olayı al
    except requests.RequestException:
        pass
    return None, None

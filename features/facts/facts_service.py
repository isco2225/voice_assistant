import requests

def fetch_random_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get("text")
        else:
            return None
    except requests.RequestException:
        return None

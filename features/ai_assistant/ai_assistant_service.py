import requests
from config.config import AI_API_URL, AI_API_KEY

def ask_to_ai(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {AI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "NousResearch/Hermes-2-Pro-Llama-3-8B",
        "messages": [
            {"role": "system", "content": "Cevabını kısa tut, yalnızca Türkçe ve anlaşılır şekilde ver."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(f"{AI_API_URL}/chat/completions", headers=headers, json=data, timeout=10)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        print(f"API Hatası: {e}")
        return "Yapay zekadan cevap alınamadı."

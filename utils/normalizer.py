import unicodedata

def normalize_text(text: str) -> str:
    replacements = {
        'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u',
    }
    text = text.lower()
    for src, target in replacements.items():
        text = text.replace(src, target)
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    return text.strip()

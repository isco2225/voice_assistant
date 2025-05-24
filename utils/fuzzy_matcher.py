from rapidfuzz import process

COMMAND_MAP = {
    "spotify aç": "spotify",
    "youtube aç": "youtube",
    "google aç": "browser",
    "tarayıcıyı aç": "browser",
    "geliştirici modu": "vs_code",
    "vs code aç": "vs_code",
    "saat kaç": "time",
    "bugün tarih": "date",
}

def match_command(text: str, threshold: int = 75) -> str | None:
    best_match, score, _ = process.extractOne(text, COMMAND_MAP.keys())
    if score >= threshold:
        return COMMAND_MAP[best_match]
    return None

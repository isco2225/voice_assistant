from rapidfuzz import process

COMMAND_MAP = {
    "spotify aç": "spotify",
    "youtube aç": "youtube",
    "tarayıcıyı aç": "browser",
    "google aç": "browser",
    "vs code aç": "vs_code",
    "geliştirici modu": "developer_mode",
    "saat kaç": "time",
    "bugün tarih": "date",
    "bilgi ver": "fact",
    "bugün ne oldu": "history_today",
    "tarihte bugün": "history_today"
}

def match_command(text: str, threshold: int = 75) -> str | None:
    best_match, score, _ = process.extractOne(text, COMMAND_MAP.keys())
    if score >= threshold:
        return COMMAND_MAP[best_match]
    return None

from rapidfuzz import process
from utils.normalizer import normalize_text


COMMAND_MAP = {
    "spotify aç": "spotify",
    "spotifyi aç": "spotify",
    "youtube aç": "youtube",
    "youtube'u aç": "youtube",
    "tarayıcıyı aç": "browser",
    "google aç": "browser",
    "vs code aç": "vs_code",
    "vscode aç": "vs_code",
    "geliştirici modu": "developer_mode",
    "yazılımcı modu": "developer_mode",
    "saat kaç": "time",
    "kaç saat": "time",
    "bugün tarih": "date",
    "bugünün tarihi": "date",
    "bilgi ver": "fact",
    "rastgele bilgi": "fact",
    "bir bilgi ver": "fact",
    "bugün ne oldu": "history_today",
    "tarihte bugün": "history_today",
    "internette araştır": "wikipedia_search",
    "wikipedia'da ara": "wikipedia_search",
    "wikipedia": "wikipedia_search",
}

def match_command(text: str, threshold: int = 75) -> str | None:
    normalized_text = normalize_text(text)
    normalized_commands = {normalize_text(cmd): val for cmd, val in COMMAND_MAP.items()}
    
    result = process.extractOne(normalized_text, normalized_commands.keys())
    if result:
        best_match, score, _ = result
        print(f"🧪 Eşleşme: {best_match} (skor: {score})")
        if score >= threshold:
            return normalized_commands[best_match]
    return None
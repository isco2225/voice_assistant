from core.interface.synthesizer import speak
from utils.normalizer import normalize_text
from utils.fuzzy_matcher import match_command
from utils.printer import customPrint, warningPrint, Emojis
from features.registry import *

COMMAND_ACTIONS = {
    "spotify": lambda: open_application("spotify"),
    "youtube": lambda: open_website("youtube"),
    "github": lambda: open_website("github"),
    "linkedin": lambda: open_website("linkedin"),
    "instagram": lambda: open_website("instagram"),
    "browser": lambda: open_website("browser"),
    "vs_code": lambda: open_application("vs_code"),
    "time": handle_time_command,
    "date": handle_date_command,
    "developer_mode": open_developer_mode,
    "fact": give_fact,
    "history_today": tell_today_in_history,
    "wikipedia_search": search_wikipedia,
    "exchange_rate": tell_exchange_rate,
    "weather": give_weather_advice,
}

def handle_command(text: str):
    normalized = normalize_text(text)
    command_key = match_command(normalized)

    if command_key:
        customPrint(Emojis.SEARCH, f"Eşleşen komut: {command_key}")
        COMMAND_ACTIONS[command_key]()
    else:
        speak("Anlayamadım.")
        warningPrint(f"Anlaşılamayan komut: {text}")

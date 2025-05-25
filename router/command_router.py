from core.synthesizer import speak
from utils.normalizer import normalize_text
from utils.fuzzy_matcher import match_command
from features.registry import *


def handle_command(text):
    normalized = normalize_text(text)
    command_key = match_command(normalized)

    print(f"🔍 Eşleşen komut: {command_key}")

    if command_key == "spotify":
        open_application("spotify")
    elif command_key == "youtube":
        open_website("youtube")
    elif command_key == "browser":
        open_website("browser")
    elif command_key == "vs_code":
        open_application("vs_code")
    elif command_key == "time":
        handle_time_command()
    elif command_key == "date":
        handle_date_command()
    elif command_key == "developer_mode":
        open_developer_mode()
    elif command_key == "fact" or any(keyword in text for keyword in ["bilgi ver", "bir bilgi ver", "rastgele bilgi"]):
        give_fact()
    elif command_key == "history_today":
        tell_today_in_history()
    else:
        speak("Anlayamadım.")
        print(f"❓ Anlaşılamayan komut: {text}")

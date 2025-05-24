from core.synthesizer import speak
from features.apps.open_app import open_application
from features.webs.open_website import open_website
from features.time_and_history.time_query import handle_time_command, handle_date_command
from utils.normalizer import normalize_text
from utils.fuzzy_matcher import match_command

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
    else:
        speak("Bu komutu anlayamadım.")
        print(f"❓ Anlaşılamayan komut: {text}")

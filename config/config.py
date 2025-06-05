import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# ------------------------------
# 🗣️ Ses Tanıma (Speech Recognition)
# ------------------------------
RECOGNITION_LANGUAGE = os.getenv("RECOGNITION_LANGUAGE", "tr-TR")
RECOGNITION_TIMEOUT = int(os.getenv("RECOGNITION_TIMEOUT", 5))
RECOGNITION_PHRASE_TIMEOUT = int(os.getenv("RECOGNITION_PHRASE_TIMEOUT", 3))

# ------------------------------
# 🔊 Sesli Yanıt (Speech Synthesis)
# ------------------------------
SYNTHESIS_LANGUAGE = os.getenv("SYNTHESIS_LANGUAGE", "tr-TR")
SYNTHESIS_RATE = int(os.getenv("SYNTHESIS_RATE", 150))
SYNTHESIS_VOLUME = float(os.getenv("SYNTHESIS_VOLUME", 1.0))

# ------------------------------
# 🗂️ Dosya Yolları
# ------------------------------
NOTES_FILE_PATH = os.getenv("NOTES_FILE_PATH", os.path.join("data", "notes.txt"))

# ------------------------------
# 🌐 API Ayarları
# ------------------------------
TRANSLATE_API_URL = os.getenv("TRANSLATE_API_URL")
FACTS_API_URL = os.getenv("FACTS_API_URL")
HISTORY_TODAY_API_URL = os.getenv("HISTORY_TODAY_API_URL")
EXCHANGE_RATE_API_URL = os.getenv("EXCHANGE_RATE_API_URL")
# ------------------------------
# 🔈 Bip Sesi Ayarları
# ------------------------------
BEEP_FREQUENCY = int(os.getenv("BEEP_FREQUENCY", 1000))
BEEP_DURATION = int(os.getenv("BEEP_DURATION", 300))

# ------------------------------
# 💬 Komutlar
# ------------------------------
EXIT_COMMANDS = os.getenv("EXIT_COMMANDS", "çık,kapat").split(",")

# ------------------------------
# 🪵 Loglama
# ------------------------------
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
LOG_FORMAT = os.getenv("LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

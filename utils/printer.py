from typing import Optional
from datetime import datetime

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Emojis:
    INFO = "ℹ️"
    SUCCESS = "✅"
    WARNING = "⚠️"
    ERROR = "❌"
    TIME = "🕒"
    DATE = "📅"
    WEATHER = "🌤"
    CLOTHES = "🧥"
    HISTORY = "📜"
    MONEY = "💰"
    KNOWLEDGE = "📚"
    SEARCH = "🔍"
    MATCH = "🎯"
    NETWORK = "🌐"
    MICROPHONE = "🎤"
    SPEAKER = "🔊"
    APP = "💻"
    WEB = "🌍"
    SYSTEM = "⚙️"
    DEBUG = "🐛"

def _get_timestamp() -> str:
    return datetime.now().strftime("%H:%M:%S")

def _format_message(emoji: str, message: str, color: Optional[str] = None) -> str:
    timestamp = _get_timestamp()
    formatted = f"{emoji} [{timestamp}] {message}"
    if color:
        formatted = f"{color}{formatted}{Colors.ENDC}"
    return formatted

def infoPrint(message: str) -> None:
    """Print an informational message."""
    print(_format_message(Emojis.INFO, message, Colors.BLUE))

def successPrint(message: str) -> None:
    """Print a success message."""
    print(_format_message(Emojis.SUCCESS, message, Colors.GREEN))

def warningPrint(message: str) -> None:
    """Print a warning message."""
    print(_format_message(Emojis.WARNING, message, Colors.WARNING))

def errorPrint(message: str) -> None:
    """Print an error message."""
    print(_format_message(Emojis.ERROR, message, Colors.FAIL))

def systemPrint(message: str) -> None:
    """Print a system-related message."""
    print(_format_message(Emojis.SYSTEM, message, Colors.CYAN))

def debugPrint(message: str) -> None:
    """Print a debug message."""
    print(_format_message(Emojis.DEBUG, message))

def customPrint(emoji: str, message: str, color: Optional[str] = None) -> None:
    """Print a custom message with specified emoji and color."""
    print(_format_message(emoji, message, color)) 
from typing import Optional
from datetime import datetime

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def _get_timestamp() -> str:
    return datetime.now().strftime("%H:%M:%S")

def _format_message(message: str, color: Optional[str] = None) -> str:
    timestamp = _get_timestamp()
    formatted = f"[{timestamp}] {message}"
    if color:
        formatted = f"{color}{formatted}{Colors.ENDC}"
    return formatted

def customPrint(message: str, color: Optional[str] = None) -> None:
    """Print a custom message with optional color."""
    print(_format_message(message, color))

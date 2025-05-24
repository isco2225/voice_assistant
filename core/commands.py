from features import notepad
from utils.logger import logger

def handle_command(command):
    """
    Handle recognized commands silently.
    Only processes known commands, ignores everything else.
    """
    if "not al" in command:
        notepad.take_note()
    # Diğer komutlar buraya eklenebilir
    # Tanınmayan komutlar sessizce görmezden gelinir
import winsound
from config.config import BEEP_FREQUENCY, BEEP_DURATION

def play_beep():
    winsound.Beep(BEEP_FREQUENCY, BEEP_DURATION)

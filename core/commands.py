from features import notepad

def handle_command(command):
    if "not al" in command:
        notepad.take_note()
    else:
        print("Komut tanınmadı.")

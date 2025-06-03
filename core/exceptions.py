class VoiceAssistantError(Exception):
    pass

class RecognitionError(VoiceAssistantError):
    def __init__(self, message="Ses algılanamadı"):
        super().__init__(message)

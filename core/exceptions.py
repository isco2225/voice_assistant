class VoiceAssistantError(Exception):
    """Tüm sesli asistan hatalarının taban sınıfı"""
    pass

class RecognitionError(VoiceAssistantError):
    """Konuşma algılamada oluşan hata"""
    def __init__(self, message="Ses algılanamadı"):
        super().__init__(message)

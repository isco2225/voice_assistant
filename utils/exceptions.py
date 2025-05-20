class VoiceAssistantError(Exception):
    pass

class RecognitionError(VoiceAssistantError):
    pass

class SynthesisError(VoiceAssistantError):
    pass

class CommandError(VoiceAssistantError):
    pass 
from core.interface.recognizer import recognize_speech
from core.interface.synthesizer import speak
from features.ai_assistant.ai_assistant_service import ask_to_ai

def ask_question_to_ai():
    speak("Evet")
    question = recognize_speech()
    print(f"Sorunuz: {question}")

    if not question:
        speak("Sorunuzu anlayamadım.")
        return

    speak("lütfen bekleyin")
    answer = ask_to_ai(question)

    if answer:
        speak(answer)
        print(f"Yapay Zeka Cevabı: {answer}")
    else:
        speak("Yapay zekadan cevap alınamadı.")


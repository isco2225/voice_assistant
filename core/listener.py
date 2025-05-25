import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(f"⚠️ [mic status] {status}")
    q.put(bytes(indata))

def listen():
    print("🎧 [listener] Vosk ile dinleme başlatıldı...")

    model = Model("vosk-model-small-tr-0.3")
    recognizer = KaldiRecognizer(model, 16000)

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("🎤 [listener] Konuşabilirsiniz...")

        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                text = json.loads(result)["text"]
                if text:
                    print(f"✅ [listener] Algılanan metin: {text}")
                    return text

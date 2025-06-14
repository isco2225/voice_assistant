import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer
from core.exceptions import RecognitionError

q = queue.Queue()
model = Model("vosk-model-small-tr-0.3")
recognizer = KaldiRecognizer(model, 16000)

def callback(indata, frames, time, status):
    if status:
        print(f"[mic status] {status}")
    q.put(bytes(indata))

def recognize_with_vosk():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "")
                if text.strip():
                    return text


import sounddevice as sd
import numpy as np

fs = 44100
duration = 5
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
print(recording)

sd.play(recording, fs)
sd.wait()
import sounddevice as sd
import numpy as np

fs = 44100
duration = 3
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
print(recording)
print(recording.shape)
sd.play(recording, fs)
sd.wait()
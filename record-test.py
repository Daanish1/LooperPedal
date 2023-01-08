# This file is testing a variable sized recording loop and
# the ability to stop the loop and start playback
import argparse
import tempfile
import queue
import sys

import sounddevice as sd
import soundfile as sf
import numpy as np
from getkey import getkey, keys

samplerate = 44100
channels = 1
filename = "test.WAV"
q = queue.Queue()

test = []

def callback(indata, frames, time, status):
    q.put(indata.copy())


with sd.InputStream(samplerate=samplerate, channels=channels,
    callback=callback):

    while True:
        # file.write(q.get())
        test.append(q.get())
        if getkey() == " ":
            break

np_list = np.array(test[-1])

sd.play(np_list, samplerate)
sd.wait()
print(np_list)
print("Im Done")



# This file is testing a variable sized recording loop and
# the ability to stop the loop and start playback
import argparse
import tempfile
import queue
import sys

import sounddevice as sd
import soundfile as sf
import numpy as np
from KeyPoller import KeyPoller


samplerate = 44100
channels = 1
q = queue.Queue()

test = []

def callback(indata, frames, time, status):
    q.put(indata.copy())


with sd.InputStream(samplerate=samplerate, channels=channels,
    callback=callback):
    with KeyPoller() as keyPoller:
        while True:
            # file.write(q.get())
            test.append(q.get())
            c = keyPoller.poll()
            if not c is None:
                    if c == " ":
                        break

        
            
        

# Pre-Proc to playback
np_list = np.array(test)
np_list = np.concatenate(np_list)


sd.play(np_list, samplerate)
sd.wait()

print("Im Done")



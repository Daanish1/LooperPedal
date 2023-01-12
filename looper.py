# Looper Pedal System
import queue
import sys

import sounddevice as sd
import soundfile as sf
import numpy as np
from KeyPoller import KeyPoller

samplerate = 44100
channels = 1
sound_queue = queue.Queue()

def callback(indata, frames, time, status):
    sound_queue.put(indata.copy())

def main():

    output_buffer = []  
    # System loop:
    # Wait for start click (space)
    print("Press Space to start")
    with KeyPoller() as keyPoller:
        while True:
            char_input = keyPoller.poll()
            if not char_input is None:
                    if char_input == " ":
                        break
    print("Recording...")
    # Record until space press
    with sd.InputStream(samplerate=samplerate, channels=channels,
        callback=callback):
        with KeyPoller() as keyPoller:
            while True:
                output_buffer.append(sound_queue.get())
                char_input = keyPoller.poll()
                if not char_input is None:
                    if char_input == " ":
                        break

    while (not sound_queue.empty()) > 0:
        output_buffer.append(sound_queue.get())
                        

    print("Looping...")
    # Loop recording until space press to stop
    np_sound = np.array(output_buffer)
    np_sound = np.concatenate(np_sound)

    while True:
        sd.play(np_sound, samplerate)
        sd.wait()
    


if __name__ == '__main__':
    main()
import pyaudio
import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import wave
import sys
import pylab as pl
import time
import threading
import queue
import math
import struct
from dataProcessing import dataCompression, dataTrain
from neural_network import test


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = .5
SHORT_NORMALIZE = (1.0/32768.0)
WAVE_OUTPUT_FILENAME = "output.wav"
THRESHOLD = .02
p = pyaudio.PyAudio()
recordingQueue = queue.Queue()
amplitudeQueue = queue.Queue()

trigger = False


def open_stream():
    """opens the pyaudio stream for recording, returns stream block"""
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    block = stream.read(CHUNK)

    stream.close()

    return block


def check_vowel(block):
    """Checks which vowel it is
        input: array of frequencies
        output: vowel"""
    output = ['A', 'E', 'O']
    data = dataCompression(block)
    test_results = nn.test(test_data)

    # position of max value in test result vector [n1, n2, n3] decides what vowel it is
    # example [1, 0, 0] - max value is at index 0 - output[0] is 'A'.
    return output[np.argmax(test_results)]


def calibration():
    """
    takes sample of screaming 3 times,
    sets the average to be the threshold value
    """
    global THRESHOLD
    shout_input = []
    time.sleep(2)
    print("Starting Calibration...")

    for i in range(3):
        print("Please SCREAM")
        time.sleep(.5)
        print("Recording")
        for i in range(50):
            shout_input.append(get_rms(open_stream()))  # stores rms in array
        print("Saving...")
    THRESHOLD = np.mean(shout_input)  # averages three rms values and sets as threshold
    print("Done calibrating. Threshold set to: {}". format(THRESHOLD))


class recordingThread(threading.Thread):
    """recording thread for main game loop, constantly checks for trigger
    and puts in thread if above threshold, also returns amplitude constantly"""
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def run(self):
        global trigger

        calibration()
        while(1):
            time.sleep(.5)  # helps to prevent simultaneous triggers
            check = check_vowel(open_stream())  # check if above threshold
            if check == 'A' or check == 'E' or check == 'O':
                trigger = True
                if recordingQueue.empty():
                    recordingQueue.put(check)  # tell main game loop triggered
            amplitudeQueue.put(True)    # always give amplitude


if __name__ == "__main__":
    calibration()
    p.terminate()

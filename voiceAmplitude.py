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

trigger = False


def get_rms(block):
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack(format, block)

    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt(sum_squares / count)


def open_stream():
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    block = stream.read(CHUNK)

    stream.close()

    return block


def check_trigger(block):
    global trigger
    amplitude = get_rms(block)
    print(amplitude)
    if amplitude > THRESHOLD:
        trigger = True

    return trigger


def record(text=True):
    global trigger
    for i in range(70):
        if text:
            print("Recording")
        if check_trigger(open_stream()):
            print("TRIGGER")
            trigger = False
        if text:
            print("Done Recording")


def calibration():
    """
    takes sample of shouting 3 times,
    sets the average to be the threshold value
    """
    global THRESHOLD
    shout_input = []
    print("Starting Calibration...")

    for i in range(3):
        print("Please SHOUT")
        time.sleep(2)
        print("Recording")
        for i in range(50):
            shout_input.append(get_rms(open_stream()))
        print("Saving...")
    THRESHOLD = np.mean(shout_input)
    print("Done calibrating. Threshold set to: {}". format(THRESHOLD))


class recordingThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def run(self):
        calibration()
        while(1):
            if check_trigger(open_stream()):
                trigger = False
                if recordingQueue.empty():
                    recordingQueue.put(True)


if __name__ == "__main__":
    calibration()
    p.terminate()

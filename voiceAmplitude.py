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
amplitudeQueue = queue.Queue()

trigger = False


def get_rms(block):
    """ calculates the RMS of the audio block to be used as the amplitude
    for the sample"""

    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack(format, block)

    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt(sum_squares / count)


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


def check_trigger(block):
    """checks for if amplitude is above the threshold"""

    global trigger
    amplitude = get_rms(block)
    if amplitude > THRESHOLD:
        trigger = True

    return trigger, amplitude


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
            time.sleep(.3)  # helps to prevent simultaneous triggers
            check = check_trigger(open_stream())  # check if above threshold
            if check[0]:
                trigger = False
                if recordingQueue.empty():
                    recordingQueue.put(True)  # tell main game loop triggered
            amplitudeQueue.put(check[1])    # always give amplitude


if __name__ == "__main__":
    calibration()
    p.terminate()

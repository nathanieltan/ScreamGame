import pyaudio
import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import wave
import sys
import pylab as pl
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = .5
WAVE_OUTPUT_FILENAME = "output.wav"
THRESHOLD = 0
p = pyaudio.PyAudio()

trigger = False


def record(record_seconds):
    """
    Records audio and returns frames to be saved to wav file
    """
    frames = []
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("*RECORDING")

    for i in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("*DONE RECORDING")

    stream.close()

    return frames


def save(frames):
    """
    takes frames and saves them to a wav file
    """
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def plot():
    """
    plots amplitude of audio input from wav file,
    can also plot power over frequency
    """
    rate, data = wav.read(WAVE_OUTPUT_FILENAME)
    t = np.arange(len(data[:, 0]))*1.0/rate
    plt.plot(t, data[:, 0])
    plt.show()

    # power = 20*np.log10(np.abs(np.fft.rfft(data[:, 0])))
    # f = np.linspace(0, rate/2.0, len(power))
    # pl.plot(f, power)
    # pl.xlabel("Frequency(Hz)")
    # pl.ylabel("Power(dB)")
    # pl.show()


def maxAmplitude(wave_file):
    """
    finds max amplitude of a wave file
    """
    rate, data = wav.read(wave_file)
    return np.amax(data[:, 0])


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
        save(record(3))
        shout_input.append(maxAmplitude(WAVE_OUTPUT_FILENAME))
        print("Saving...")
    THRESHOLD = np.mean(shout_input)
    print("Done calibrating. Threshold set to: {}". format(THRESHOLD))


def check_trigger():
    """
    Check to see if audio input goes above threshold,
    returns bool
    """
    global trigger
    save(record(RECORD_SECONDS))
    max_amp = maxAmplitude(WAVE_OUTPUT_FILENAME)

    print("Max Amplitude: {}".format(max_amp))
    if max_amp >= THRESHOLD:
        trigger = True
    return trigger


if __name__ == "__main__":
    calibration()
    for i in range(20):  # records for 10 seconds
        if check_trigger():
            print('FALL')
            trigger = False
    p.terminate()

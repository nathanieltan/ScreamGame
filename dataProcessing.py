import numpy as np
from scipy.io import wavfile

f = open('sound.txt')
soundFiles = f.read().split()
f.close()

max = len(soundFiles)
i = 0

allData = []
output = []

while i < max - 1:
    fs, data = wavfile.read(soundFiles[i])
    allData.append(np.sin(data))
    if soundFiles[i + 1] == 'a':
        output.append([1, 0, 0])
    elif soundFiles[i + 1] == 'e':
        output.append([0, 1, 0])
    elif soundFiles[i + 1] == 'o':
        output.append([0, 0, 1])
    i += 2

outputData = [[d] + [o] for d, o in zip(allData, output)]

print(outputData)

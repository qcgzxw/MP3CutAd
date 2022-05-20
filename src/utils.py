from scipy.io import wavfile
from scipy.fftpack import rfft
import numpy as np

LEN = 128
STEP = 2205


def wav_fft(filename: str) -> any:
    rate, data = wavfile.read(filename)
    data_length = len(data) - 44
    result = np.zeros((int((data_length - LEN) / STEP) + 1, int(LEN/2)), dtype=int)
    for i in range(44, len(data), STEP):
        cnt = int((i-44) / STEP)
        v = np.zeros(LEN)
        c = np.zeros(LEN)
        total = STEP * 2
        if i + total > data_length:
            total = data_length - i
        for j in range(total):
            k = int(j * LEN / total)
            v[k] += data[i + j]
            c[k] += 1
        for j in range(LEN):
            v[j] = int(v[j] / c[j])
        v = rfft(v)
        for j in range(int(len(v)/2)):
            result[cnt][j] = abs(v[j])

    with open(filename + ".fft", 'w') as f:
        for d in result:
            f.writelines(str(d))
    return result

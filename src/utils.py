from scipy.io import wavfile as wav
from scipy.fftpack import rfft


def wav_fft(filename: str) -> any:
    rate, data = wav.read(filename)
    return rfft(data)

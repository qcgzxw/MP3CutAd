from unittest import TestCase
from .utils import wav_fft, is_save_wav,lsh_em


class Test(TestCase):
    def test_wav_fft(self):
        fft = wav_fft("test1-2.wav")
        a = []
        print(fft[0], fft[1], fft[2], fft[3])
        for d in fft:
            if d != 0:
                a.append(d)

        print(len(fft))
        print(len(a))

    def test_is_save_wav(self):
        is_save_wav("test1-2.wav", "test2-4.wav")

    def test_is_save_wav(self):
        lsh_em()


import os
from unittest import TestCase
from .utils import wav_fft
from .ffmpeg import FFMpeg

DEMO1_PATH = "test/demo1.m4a"
DEMO1_WAV_PATH = "test/demo1.wav"
DEMO2_PATH = "test/demo2.m4a"
DEMO2_WAV_PATH = "test/demo2.wav"
DEMO3_PATH = "test/demo3.m4a"
DEMO3_WAV_PATH = "test/demo3.wav"


class Test(TestCase):

    def setUp(self) -> None:
        if not os.path.isfile(DEMO1_WAV_PATH):
            FFMpeg(DEMO1_PATH).audio2wav(DEMO1_WAV_PATH)
        if not os.path.isfile(DEMO2_WAV_PATH):
            FFMpeg(DEMO2_PATH).audio2wav(DEMO2_WAV_PATH)
        if not os.path.isfile(DEMO3_WAV_PATH):
            FFMpeg(DEMO3_PATH).audio2wav(DEMO3_WAV_PATH)

    def tearDown(self) -> None:
        if os.path.isfile(DEMO1_WAV_PATH):
            os.remove(DEMO1_WAV_PATH)
        if os.path.isfile(DEMO2_WAV_PATH):
            os.remove(DEMO2_WAV_PATH)
        if os.path.isfile(DEMO3_WAV_PATH):
            os.remove(DEMO3_WAV_PATH)

    def test_wav_fft(self):
        fft1 = wav_fft(DEMO1_WAV_PATH)
        fft2 = wav_fft(DEMO2_WAV_PATH)
        print(len(fft1[0]))
        print(len(fft2[0]))
        print(fft2[45])
        print(len(fft1))
        print(len(fft2))


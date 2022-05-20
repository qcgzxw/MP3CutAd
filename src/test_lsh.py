import itertools
import os
import time
from unittest import TestCase
from .lsh import LSH
from .utils import wav_fft
from .ffmpeg import FFMpeg

DEMO1_PATH = "test/demo1.m4a"
DEMO1_WAV_PATH = "test/demo1.wav"
DEMO2_PATH = "test/demo2.m4a"
DEMO2_WAV_PATH = "test/demo2.wav"
DEMO3_WAV_PATH = "test/demo3.wav"
STEP = 1


class TestLSH(TestCase):

    def setUp(self) -> None:
        if not os.path.isfile(DEMO1_WAV_PATH):
            FFMpeg(DEMO1_PATH).audio2wav(DEMO1_WAV_PATH)
        if not os.path.isfile(DEMO2_WAV_PATH):
            FFMpeg(DEMO2_PATH).audio2wav(DEMO2_WAV_PATH)

        start_time = time.perf_counter()
        dasdwq = wav_fft(DEMO1_WAV_PATH)
        self.lsh = LSH()
        print("fft时间:")
        print(time.perf_counter() - start_time)
        start_time = time.perf_counter()
        for index in range(len(dasdwq)):
            self.lsh.insert(str(index), list(itertools.chain(*dasdwq[index:index+STEP])))

        print("lsh插入时间:")
        print(time.perf_counter() - start_time)

    def tearDown(self) -> None:
        if os.path.isfile(DEMO1_WAV_PATH):
            os.remove(DEMO1_WAV_PATH)
        if os.path.isfile(DEMO2_WAV_PATH):
            os.remove(DEMO2_WAV_PATH)

    def testQuery(self):
        if not os.path.isfile(DEMO2_WAV_PATH):
            FFMpeg(DEMO2_PATH).audio2wav(DEMO2_WAV_PATH, "8000")
        result = {}
        start_time = time.perf_counter()
        dasdwq = wav_fft(DEMO2_WAV_PATH)
        print("fft时间:")
        print(time.perf_counter() - start_time)
        start_time = time.perf_counter()
        for index in range(len(dasdwq)):
            r = self.lsh.query(list(itertools.chain(*dasdwq[index:index+STEP])))
            if len(r) > 0:
                result[index] = r

        print(len(result))
        print(dict(sorted(result.items())))
        print("查询时间:")
        print(time.perf_counter() - start_time)



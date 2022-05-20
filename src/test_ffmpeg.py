from unittest import TestCase
from .ffmpeg import FFMpeg

DEMO1_PATH = "test/demo1.m4a"
DEMO1_WAV_PATH = "test/demo1.mp3"
DEMO2_PATH = "test/demo2.m4a"
DEMO2_WAV_PATH = "test/demo2.mp3"
DEMO3_PATH = "test/demo3.m4a"
DEMO3_WAV_PATH = "test/demo3.mp3"


class TestFFMpeg(TestCase):
    def test_audio2wav(self):
        FFMpeg(DEMO1_PATH).audio2wav(DEMO1_WAV_PATH)
        FFMpeg(DEMO2_PATH).audio2wav(DEMO2_WAV_PATH)
        FFMpeg(DEMO3_PATH).audio2wav(DEMO3_WAV_PATH)

    def test_split(self):
        f1 = FFMpeg(DEMO1_WAV_PATH)
        f2 = FFMpeg(DEMO2_WAV_PATH)
        f3 = FFMpeg(DEMO3_WAV_PATH)
        for i in range(0, 15, 5):
            f1.split(DEMO1_WAV_PATH + str(i) + "-" + str(i+5) + ".mp3", float(i), float(i+5))
            f2.split(DEMO2_WAV_PATH + str(i) + "-" + str(i+5) + ".mp3", float(i), float(i+5))
            f3.split(DEMO3_WAV_PATH + str(i) + "-" + str(i+5) + ".mp3", float(i), float(i+5))

    def test_cut_ad(self):
        f = FFMpeg("test.mp3")
        ad_list = [(0.0, 3.22), (7.88, 10.92), (15.22, 17.00), (20.33, 31.22), (40.00, 200.00), (235.768163, 251.768163)]
        f.cut_ad(ad_list, "test_new.mp3")

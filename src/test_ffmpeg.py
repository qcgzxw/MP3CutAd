from unittest import TestCase
from .ffmpeg import FFMpeg


class TestFFMpeg(TestCase):
    def test_audio2wav(self):
        f = FFMpeg("test.mp3")
        f.audio2wav("test.wav")

    def test_split(self):
        f = FFMpeg("test.wav")
        f.split('test1-2.wav', 1.0, 2.0)
        for index in range(int(float(f.info['format']['duration']))):
            f.split('test/test' + str(index) + '.wav', float(index), float(index+1))

    def test_cut_ad(self):
        f = FFMpeg("test.mp3")
        ad_list = [(0.0, 3.22), (7.88, 10.92), (15.22, 17.00), (20.33, 31.22), (40.00, 200.00), (235.768163, 251.768163)]
        f.cut_ad(ad_list, "test_new.mp3")


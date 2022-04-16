import os
from unittest import TestCase
from .lsh import LSH
from .utils import wav_fft


class TestLSH(TestCase):

    def setUp(self) -> None:
        self.lsh = LSH(2205)
        for _, _, files in os.walk('test'):
            for file in files:
                index = file.replace("test", "", 1).replace('.wav', '', 1)
                self.lsh.insert(index, wav_fft("test/" + file))

    def testQuery(self):
        print(self.lsh.query(wav_fft("test1-2.wav")))



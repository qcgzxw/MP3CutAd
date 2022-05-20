import os.path
import tempfile

from .types import AdList, AudioList
from .ffmpeg import FFMpeg
from .lsh import LSH
from .utils import wav_fft
from .exception import AudioException

PENDING = 0
AD_SCANNING = 1
AD_SCANNED = 2
AD_CUT_PROCESSING = 3
AD_CUT_PROCESSED = 4
ERROR = -1


class Audio:
    filename = str
    ad_list = AdList
    status = PENDING
    lsh = LSH

    def __init__(self, filename: str, ):
        self.filename = filename
        self.ffmpeg = FFMpeg(self.filename)
        self.info = self.ffmpeg.get_format_info()
        self.check()

    def __del__(self):
        pass

    def check(self):
        if not self.info or float(self.info.duration) == 0:
            self.status = ERROR

    def lsh_calculate(self, step: int = 2205) -> None:
        self.status = AD_SCANNING
        self.lsh = LSH(step)
        with tempfile.TemporaryDirectory() as tmp_dirname:
            def _get_tmp_file(filename: str) -> str:
                return tmp_dirname + os.path.sep + filename

            def _split():
                for i in range(int(float(self.info.duration))):
                    self.ffmpeg.split(_get_tmp_file(str(i)), float(i), float(i + 1))

            _split()
            for _, _, files in os.walk(tmp_dirname):
                for file in files:
                    self.lsh.insert(file, wav_fft(tmp_dirname + os.sep + file))
        self.status = AD_SCANNED

    def cut_ad(self, output_dir: str, path: str) -> None:
        self.status = AD_CUT_PROCESSING
        if path == "":
            if not os.path.isdir(output_dir):
                os.mkdir(output_dir)
            path = output_dir + os.sep + self.filename
        self.ffmpeg.cut_ad(self.ad_list, path)
        self.status = AD_CUT_PROCESSED


def compare(simple_audio: Audio, audio_list: AudioList) -> AudioList:
    """
    比较
    :param simple_audio: 样本音频
    :param audio_list: 待比较的音频
    :return : 音频列表
    """
    if simple_audio.status < AD_SCANNED:
        raise AudioException('样本文件未扫描')
    for audio in audio_list:
        pass
        #simple_audio.lsh.

    return audio_list

from .types import AdList, AudioList, StreamList

import ffmpeg


class FFMpeg:
    def __init__(self, filename: str):
        self.filename = filename
        self.input = ffmpeg.input(filename)
        self.info = ffmpeg.probe(filename)

    def audio2wav(self, output: str) -> None:
        self.input.output(output, ac="1", ar="22050", f="wav").global_args('-y', '-loglevel', '0').run()

    def split(self, output: str, start: float, end: float) -> None:
        # 禁止-c copy 解决时长不准确问题
        if end <= start:
            return
        self.input.output(output, ss=str(start), to=str(end)) \
            .global_args('-y', '-loglevel', '0').run()

    def concat(self, audio_list: AudioList, output: str) -> None:
        stream_list: StreamList = []
        for index in range(len(audio_list)):
            start, end = audio_list[index]
            stream_list.append(ffmpeg.input(self.filename, ss=str(start), to=str(end)))
        ffmpeg.concat(*stream_list, v=0, a=1, n=len(stream_list)).output(output, f="mp3")\
            .global_args('-y', '-loglevel', '0').run()

    def cut_ad(self, ad_list: AdList, output: str) -> None:
        if len(ad_list) == 0:
            return
        audio_list: AudioList = []
        if ad_list[0][0] > 0:
            audio_list.append((0, ad_list[0][0]))
        duration = float(self.info['format']['duration'])
        for index in range(len(ad_list)):
            is_first = index == 0
            is_last = index == len(ad_list) - 1
            ad_start, ad_end = ad_list[index]
            if is_first and ad_start > 0:
                audio_list.append((0, ad_start))
            start = ad_end
            end = ad_list[index + 1][0] if not is_last else duration
            if end > start > 0:
                audio_list.append((start, end))
        self.concat(audio_list, output)

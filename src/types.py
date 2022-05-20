from typing import List, Tuple
from .audio import Audio

import ffmpeg

AdList = List[Tuple[float, float]]
StreamList = List[ffmpeg.Stream]
AudioList = List[Audio]

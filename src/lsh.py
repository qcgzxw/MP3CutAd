from datasketch.minhash import MinHash
from datasketch.lsh import MinHashLSH


def _get_hash(data: list, step=1) -> MinHash:
    t = MinHash(num_perm=128)
    for p in range(int(len(data) / step)):
        t.update(data[p * step])
    return t


class LSH:
    def __init__(self, step: int = 2205):
        # wav频率22050hz，默认只取100个点，减少计算量
        self.step = step
        self.samples = MinHashLSH(threshold=0.5, num_perm=128)

    def insert(self, key: str, data: list) -> None:
        self.samples.insert(key, _get_hash(data, self.step))

    def query(self, data: list) -> list:
        return self.samples.query(_get_hash(data, self.step))

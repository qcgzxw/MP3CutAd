from datasketch.minhash import MinHash
from datasketch.lsh import MinHashLSH


def _get_hash(data: list) -> MinHash:
    t = MinHash()
    for d in data:
        t.update(d)
    return t


class LSH:
    def __init__(self):
        self.samples = MinHashLSH(threshold=0.5)

    def insert(self, key: str, data: list) -> None:
        self.samples.insert(key, _get_hash(data))

    def query(self, data: list):
        hash_data = _get_hash(data)
        r = self.samples.query(hash_data)
        if len(r) > 0:
            print(len(r))
            print(r)

        return r

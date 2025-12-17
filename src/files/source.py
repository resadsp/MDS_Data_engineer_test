import random
from .file import File

class FileSource:
    def __init__(self, count: int = 0, avg_size: int = 0):
        self.count = count
        self.avg_size = avg_size
        self._callbacks = []

    def _generate_files(self):
        for i in range(self.count):
            size = max(1, int(random.expovariate(1/self.avg_size)))
            yield File(size_bytes=size, name=f"file_{i}")

    def subscribe(self, callback):
        self._callbacks.append(callback)

    def start(self):
        for f in self._generate_files():
            for cb in self._callbacks:
                cb(f)

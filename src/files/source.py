# src/files/source.py
import random
import string
from typing import Callable, List
from .file import File
import numpy as np

# src/files/source.py

class FileSource:
    def __init__(self, count: int = 0, avg_size: int = 0):
        self.count = count
        self.avg_size = avg_size

    def _generate_files(self):
        import random
        for i in range(self.count):
            size = int(random.expovariate(1/self.avg_size))
            yield File(size_bytes=size)

    def start(self, callback):
        for f in self._generate_files():
            callback(f)

# src/files/source.py
import random
import string
from typing import Callable, List
from .file import File
import numpy as np

class FileSource:
    def __init__(self, num_files: int = 100, mean_size_bytes: int = 1024*1024):
        self.num_files = num_files
        self.mean_size_bytes = mean_size_bytes
        self.subscribers: List[Callable[[File], None]] = []

    def subscribe(self, callback: Callable[[File], None]):
        self.subscribers.append(callback)

    def start(self):
        for i in range(self.num_files):
            size = int(np.random.exponential(self.mean_size_bytes))
            name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            file = File(name=name, size_bytes=size)
            for callback in self.subscribers:
                callback(file)

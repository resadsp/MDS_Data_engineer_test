# src/files/bucketing_strategy.py
from abc import ABC, abstractmethod
from typing import List
from .file import File

class BucketingStrategy(ABC):
    @abstractmethod
    def create_buckets(self, files: List[File]) -> List[List[File]]:
        pass

class MaxSizeStrategy(BucketingStrategy):
    def __init__(self, max_size_bytes: int):
        self.max_size_bytes = max_size_bytes

    def create_buckets(self, files: List[File]) -> List[List[File]]:
        buckets = []
        current_bucket = []
        current_size = 0

        for f in files:
            if current_size + f.size_bytes > self.max_size_bytes:
                if current_bucket:
                    buckets.append(current_bucket)
                current_bucket = [f]
                current_size = f.size_bytes
            else:
                current_bucket.append(f)
                current_size += f.size_bytes

        if current_bucket:
            buckets.append(current_bucket)
        return buckets

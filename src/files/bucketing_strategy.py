from abc import ABC, abstractmethod
from typing import List
from files.file import File

class BucketingStrategy(ABC):
    def __init__(self, target_size: int):
        self.target_size = target_size

    @abstractmethod
    def bucketize(self, files: List[File]) -> List[List[File]]:
        pass

class SimpleBucketingStrategy(BucketingStrategy):
    def bucketize(self, files: List[File]) -> List[List[File]]:
        buckets = []
        current = []
        current_sum = 0
        for f in files:
            if current and (current_sum + f.size_bytes) > self.target_size:
                buckets.append(current)
                current = []
                current_sum = 0
            if f.size_bytes > self.target_size:
                buckets.append([f])
                continue
            current.append(f)
            current_sum += f.size_bytes
        if current:
            buckets.append(current)
        return buckets

class FirstFitBucketingStrategy(BucketingStrategy):
    def bucketize(self, files: List[File]) -> List[List[File]]:
        buckets: List[List[File]] = []
        for f in files:
            placed = False
            for bucket in buckets:
                if sum(x.size_bytes for x in bucket) + f.size_bytes <= self.target_size:
                    bucket.append(f)
                    placed = True
                    break
            if not placed:
                buckets.append([f])
        return buckets

# Alias za demo
MaxSizeStrategy = SimpleBucketingStrategy

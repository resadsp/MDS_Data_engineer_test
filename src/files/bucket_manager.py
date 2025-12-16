# src/files/bucket_manager.py
from typing import List
from .file import File
from .bucketing_strategy import BucketingStrategy, MaxSizeStrategy
from .bucket import BucketTask
from core.worker_pool import WorkerPool

class BucketManager:
    def __init__(self, worker_pool: WorkerPool, strategy: BucketingStrategy):
        self.worker_pool = worker_pool
        self.strategy = strategy
        self.pending_files: List[File] = []

    def add_file(self, file: File):
        self.pending_files.append(file)
        self._check_and_submit_buckets()

    def _check_and_submit_buckets(self):
        buckets = self.strategy.create_buckets(self.pending_files)
        # Submit all full buckets to WorkerPool, keep remaining in pending_files
        full_buckets = buckets[:-1] if buckets else []
        remaining_bucket = buckets[-1] if buckets else []

        for bucket in full_buckets:
            task = BucketTask(bucket)
            self.worker_pool.submit(task)

        self.pending_files = remaining_bucket

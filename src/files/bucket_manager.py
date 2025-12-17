from .bucketing_strategy import BucketingStrategy
from .bucket import BucketTask
import threading

class BucketManager:
    def __init__(self, worker_pool, strategy: BucketingStrategy):
        self.worker_pool = worker_pool
        self.strategy = strategy
        self.pending_files = []
        self._lock = threading.Lock()

    def add_file(self, f):
        with self._lock:
            self.pending_files.append(f)
            self._check_and_submit_buckets()

    def _check_and_submit_buckets(self):
        buckets = self.strategy.bucketize(self.pending_files)
        self.pending_files = []
        for bucket in buckets:
            self.worker_pool.submit(BucketTask(bucket, None))

from files.bucket_manager import BucketManager
from files.bucketing_strategy import SimpleBucketingStrategy
from core.worker_pool import WorkerPool
from files.file import File

def test_bucket_manager_no_files():
    pool = WorkerPool(max_workers=1)
    manager = BucketManager(pool, SimpleBucketingStrategy(target_size=10))
    # no files added, flush should not fail
    pool.shutdown()

import time
from core.worker_pool import WorkerPool
from files.source import FileSource
from files.bucket_manager import BucketManager
from files.bucketing_strategy import MaxSizeStrategy

def main():
    pool = WorkerPool(max_workers=5)
    strategy = MaxSizeStrategy(target_size=10*1024*1024)
    manager = BucketManager(worker_pool=pool, strategy=strategy)
    source = FileSource(count=10, avg_size=1024*1024)
    source.subscribe(manager.add_file)
    source.start()
    time.sleep(1)
    pool.shutdown()

if __name__ == "__main__":
    main()

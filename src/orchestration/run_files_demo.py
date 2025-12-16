# src/orchestration/run_files_demo.py
import time
from core.worker_pool import WorkerPool
from files.source import FileSource
from files.bucket_manager import BucketManager
from files.bucketing_strategy import MaxSizeStrategy

def main():
    # Kreiramo WorkerPool sa 10 thread-ova
    pool = WorkerPool(max_workers=10)

    # Kreiramo Bucketing strategiju
    strategy = MaxSizeStrategy(max_size_bytes=10 * 1024 * 1024)  # 10MB

    # Kreiramo BucketManager
    manager = BucketManager(worker_pool=pool, strategy=strategy)

    # Kreiramo FileSource
    source = FileSource(num_files=100, mean_size_bytes=1024*1024)  # 1MB prosečno
    source.subscribe(manager.add_file)

    # Startujemo izvor fajlova
    print("[Demo] File processing started...")
    source.start()

    # Dajemo vremena da se završe svi taskovi
    time.sleep(3)
    print("[Demo] Finished file processing demo.")

if __name__ == "__main__":
    main()

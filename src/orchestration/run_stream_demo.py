import time
from core.worker_pool import WorkerPool
from stream.message_source import MessageSource
from stream.minibatch_builder import MiniBatchBuilder

def main():
    pool = WorkerPool(max_workers=5)
    builder = MiniBatchBuilder(worker_pool=pool, window_seconds=10)
    source = MessageSource(rate_per_minute=60)
    source.subscribe(builder.add_message)
    source.start()
    time.sleep(1)
    pool.shutdown()

if __name__ == "__main__":
    main()

import time
from core.worker_pool import WorkerPool
from stream.message_source import MessageSource
from stream.minibatch_builder import MiniBatchBuilder

def main():
    # Kreiramo WorkerPool sa 10 thread-ova
    pool = WorkerPool(max_workers=10)

    # Kreiramo MiniBatchBuilder
    builder = MiniBatchBuilder(worker_pool=pool, window_seconds=10)  # za testiranje 10s umesto 5min

    # Kreiramo MessageSource
    source = MessageSource(rate_per_minute=60)  # ~1 msg/sec za demo
    source.subscribe(builder.add_message)

    # Startujemo izvor poruka
    source.start()

    # Demo traje 30 sekundi
    print("[Demo] Streaming started...")
    time.sleep(30)
    print("[Demo] Finished demo.")

if __name__ == "__main__":
    main()

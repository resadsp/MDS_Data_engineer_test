from typing import Optional
from stream.minibatch import MiniBatch
from core.worker_pool import WorkerPool
from stream.minibatch_task import MiniBatchTask
import threading

class MiniBatchBuilder:
    def __init__(self, worker_pool, window_seconds: int):
        self.worker_pool = worker_pool
        self.window_seconds = window_seconds
        self.current_batch = MiniBatch()
        self._lock = threading.Lock()

    def add_message(self, msg):
        with self._lock:
            self.current_batch.add(msg)

    def _flush(self):
        with self._lock:
            if len(self.current_batch) > 0:
                print(f"[MiniBatchBuilder] Flushing batch of {len(self.current_batch)} messages")
                self.worker_pool.submit(MiniBatchTask(self.current_batch))
            self.current_batch = MiniBatch()

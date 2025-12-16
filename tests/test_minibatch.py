import pytest
from stream.minibatch import MiniBatch
from stream.message import Message
from stream.minibatch_builder import MiniBatchBuilder
from core.worker_pool import WorkerPool
from stream.minibatch_task import MiniBatchTask
import threading

def test_minibatch_empty():
    batch = MiniBatch()
    assert len(batch) == 0

def test_minibatch_add():
    batch = MiniBatch()
    batch.add(Message("x"))
    assert len(batch) == 1
    assert batch.messages[0].value == "x"

def test_minibatch_builder_thread_safety():
    pool = WorkerPool(max_workers=2)
    builder = MiniBatchBuilder(pool, window_seconds=0)

    def add_msgs():
        for i in range(10):
            builder.add_message(Message(f"msg{i}"))

    threads = [threading.Thread(target=add_msgs) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    builder._flush()  # should submit without error
    pool.shutdown()

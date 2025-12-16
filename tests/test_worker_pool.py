import pytest
import time
from core.worker_pool import WorkerPool
from core.task import Task

class DummyTask(Task):
    def __init__(self):
        self.executed = False

    def execute(self):
        self.executed = True

def test_worker_pool_executes_tasks():
    pool = WorkerPool(max_workers=2)
    tasks = [DummyTask() for _ in range(5)]
    for t in tasks:
        pool.submit(t)
    time.sleep(0.2)
    assert all(t.executed for t in tasks)
    pool.shutdown()

from concurrent.futures import ThreadPoolExecutor, Future
from typing import List
from .task import Task

class WorkerPool:
    """
    Executes Task instances concurrently using ThreadPoolExecutor.
    """

    def __init__(self, max_workers: int = 10):
        self._executor = ThreadPoolExecutor(max_workers=max_workers)

    def submit(self, task: Task) -> Future:
        print(f"[WorkerPool] Submitting task: {task}")
        return self._executor.submit(task.execute)

    def shutdown(self, wait: bool = True):
        print("[WorkerPool] Shutting down")
        self._executor.shutdown(wait=wait)

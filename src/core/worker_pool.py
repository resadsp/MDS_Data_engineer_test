from concurrent.futures import ThreadPoolExecutor, Future
from .task import Task

class WorkerPool:
    def __init__(self, max_workers: int = 10):
        self._executor = ThreadPoolExecutor(max_workers=max_workers)

    def submit(self, task: Task) -> Future:
        return self._executor.submit(task.execute)

    def shutdown(self, wait: bool = True):
        self._executor.shutdown(wait=wait)

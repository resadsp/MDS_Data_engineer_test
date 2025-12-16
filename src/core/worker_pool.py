from concurrent.futures import ThreadPoolExecutor, Future
from typing import List
from .task import Task

class WorkerPool:
    """
    Simple worker pool that executes Task instances concurrently.
    """

    def __init__(self, max_workers: int = 10):
        self._executor = ThreadPoolExecutor(max_workers=max_workers)

    def submit(self, task: Task) -> Future:
        """
        Submit a Task to the pool for execution.
        """
        return self._executor.submit(task.execute)

    def shutdown(self, wait: bool = True):
        """
        Shutdown the pool.
        """
        self._executor.shutdown(wait=wait)

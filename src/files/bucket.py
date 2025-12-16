from typing import List
from .file import File
from core.task import Task

class BucketTask(Task):
    def __init__(self, files: List[File]):
        self.files = files

    def execute(self):
        print(f"[BucketTask] Processing bucket with {len(self.files)} files, total size: {sum(f.size_bytes for f in self.files)}B")
        for f in self.files:
            pass

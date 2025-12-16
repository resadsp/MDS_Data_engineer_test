from core.task import Task

class BucketTask(Task):
    def __init__(self, files):
        self.files = files

    def execute(self):
        total = sum(f.size_bytes for f in self.files)
        print(f"[BucketTask] Processing bucket of {len(self.files)} files, total size: {total}B")

    def __repr__(self):
        return f"BucketTask({len(self.files)} files)"

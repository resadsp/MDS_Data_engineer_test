class Bucket:
    def __init__(self, files=None):
        self.files = files or []

    def add_file(self, f):
        self.files.append(f)

    @property
    def total_size(self):
        return sum(f.size_bytes for f in self.files)

class BucketTask:
    def __init__(self, bucket, file=None):
        self.bucket = bucket
        self.file = file

import pytest
from files.source import FileSource
from files.bucketing_strategy import SimpleBucketingStrategy
from files.bucket_manager import BucketManager

def test_file_source_generates(monkeypatch):
    generated = []
    monkeypatch.setattr(FileSource, "start", lambda self: [generated.append(f) for f in self._generate_files()])
    src = FileSource(count=5, avg_size=100)
    src.start()
    assert len(generated) == 5

def test_bucket_manager_submits(monkeypatch):
    submitted = []
    class FakePool:
        def submit(self, task):
            submitted.append(task)
    manager = BucketManager(worker_pool=FakePool(), strategy=SimpleBucketingStrategy(target_size=10))
    for _ in range(10):
        manager.add_file(type("F", (), {"size_bytes": 1})())
    assert submitted

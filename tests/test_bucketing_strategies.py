import pytest
from files.bucketing_strategy import SimpleBucketingStrategy, FirstFitBucketingStrategy
from files.file import File

@pytest.fixture
def many_small_files():
    # 5 files of 1 byte each
    return [File(size_bytes=1) for _ in range(5)]

@pytest.fixture
def mixed_files():
    # small and large
    return [File(size_bytes=8), File(size_bytes=3), File(size_bytes=7), File(size_bytes=1)]

def test_simple_bucketing_basic(many_small_files):
    strat = SimpleBucketingStrategy(target_size=3)
    buckets = strat.bucketize(many_small_files)
    # Each bucket should have at most 3 bytes
    assert all(sum(f.size_bytes for f in b) <= 3 for b in buckets)
    # All files must be present
    assert sum(len(b) for b in buckets) == 5

def test_simple_bucketing_order(mixed_files):
    strat = SimpleBucketingStrategy(target_size=10)
    buckets = strat.bucketize(mixed_files)
    flat = [f.size_bytes for b in buckets for f in b]
    # Order should be preserved
    assert flat == [8, 3, 7, 1]

def test_firstfit_bucketing(many_small_files):
    strat = FirstFitBucketingStrategy(target_size=2)
    buckets = strat.bucketize(many_small_files)
    # Because we use first fit, more packing happens
    assert len(buckets) <= len(many_small_files)

def test_firstfit_bucketing_mixed(mixed_files):
    strat = FirstFitBucketingStrategy(target_size=8)
    buckets = strat.bucketize(mixed_files)
    # Should fit 7 and 1 in one buffer if possible
    sizes = [sum(f.size_bytes for f in b) for b in buckets]
    assert all(s <= 8 for s in sizes)

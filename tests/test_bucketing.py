import pytest
from files.file import File
from files.bucketing_strategy import SimpleBucketingStrategy, FirstFitBucketingStrategy

def test_simple_strategy_large_file():
    files = [File(10), File(50)]
    strat = SimpleBucketingStrategy(target_size=20)
    buckets = strat.bucketize(files)
    assert buckets[0] == [files[0]]
    assert buckets[1] == [files[1]]  # large file alone

def test_firstfit_order_preserved():
    files = [File(5), File(3), File(7)]
    strat = FirstFitBucketingStrategy(target_size=10)
    buckets = strat.bucketize(files)
    flattened = [f.size_bytes for b in buckets for f in b]
    assert flattened == [5, 3, 7]

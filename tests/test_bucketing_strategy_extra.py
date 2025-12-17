from files.bucketing_strategy import SimpleBucketingStrategy
from files.file import File

def test_bucketize_empty_list():
    strat = SimpleBucketingStrategy(target_size=10)
    buckets = strat.bucketize([])
    assert buckets == []

def test_bucketize_edge_case():
    files = [File(5), File(5)]
    strat = SimpleBucketingStrategy(target_size=5)
    buckets = strat.bucketize(files)
    # Provjeravamo da su svi files ubačeni u neki bucket
    all_files = [f for b in buckets for f in b]
    assert sorted(f.size_bytes for f in all_files) == [5, 5]

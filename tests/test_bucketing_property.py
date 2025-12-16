from hypothesis import given, strategies as st
from files.file import File
from files.bucketing_strategy import SimpleBucketingStrategy

@st.composite
def files_lists(draw):
    sizes = draw(st.lists(st.integers(min_value=0, max_value=1), max_size=10))
    return [File(s) for s in sizes]

@given(files_lists(), st.integers(min_value=1, max_value=100))
def test_simple_bucket_properties(files, target):
    strat = SimpleBucketingStrategy(target_size=target)
    buckets = strat.bucketize(files)
    all_files = [f for b in buckets for f in b]
    assert sorted([f.size_bytes for f in all_files]) == sorted([f.size_bytes for f in files])


@given(file_lists(), st.integers(min_value=2, max_value=20))
def test_firstfit_bucket_properties(files, target):
    strat = FirstFitBucketingStrategy(target_size=target)
    buckets = strat.bucketize(files)

    for b in buckets:
        total = sum(f.size_bytes for f in b)
        assert total <= target

    all_files = [f for b in buckets for f in b]
    assert sorted([f.size_bytes for f in all_files]) == sorted([f.size_bytes for f in files])

from hypothesis import given, settings, HealthCheck
import hypothesis.strategies as st  # <-- ovo je ključno
from files.file import File
from files.bucketing_strategy import SimpleBucketingStrategy

@st.composite
def files_lists(draw):
    # generiši listu File objekata sa veličinama 0 ili 1 i do 10 elemenata
    sizes = draw(st.lists(st.integers(min_value=0, max_value=1), max_size=10))
    return [File(size_bytes=s) for s in sizes]

# Suppress HealthCheck.too_slow da Hypothesis ne blokira test
@settings(suppress_health_check=[HealthCheck.too_slow])
@given(files_lists(), st.integers(min_value=1, max_value=100))
def test_simple_bucket_properties(files, target):
    strat = SimpleBucketingStrategy(target_size=target)
    buckets = strat.bucketize(files)
    all_files = [f for b in buckets for f in b]
    assert sorted([f.size_bytes for f in all_files]) == sorted([f.size_bytes for f in files])


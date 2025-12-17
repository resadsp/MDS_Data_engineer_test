from files.file import File
from files.bucket import Bucket

def test_bucket_add_and_total():
    bucket = Bucket()
    f1 = File(size_bytes=100, name="file1")
    f2 = File(size_bytes=200, name="file2")

    # Koristimo ispravnu metodu iz Bucket klase
    bucket.add_file(f1)
    bucket.add_file(f2)

    assert bucket.total_size == 300
    assert bucket.files == [f1, f2]

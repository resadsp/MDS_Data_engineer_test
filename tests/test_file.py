from src.files.file import File

def test_file_creation():
    f = File(1234, "myfile")
    assert f.size_bytes == 1234
    assert f.name == "myfile"


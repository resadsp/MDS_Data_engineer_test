import pytest
from files.file import File

def test_file_negative_size():
    with pytest.raises(ValueError):
        File(-1)

def test_file_default_name():
    f = File(10)
    assert f.name is None or isinstance(f.name, str)

import pytest
from src.files.source import FileSource
from src.files.file import File

class FileSource:
    def __init__(self, files):
        self.files = files

    def read(self):
        for f in self.files:
            yield f


def test_file_source_reads():
    files = [File(1, "a"), File(2, "b")]
    source = FileSource(files)
    out = list(source.read())
    assert out == files

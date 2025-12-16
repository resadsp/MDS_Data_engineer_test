# src/files/file.py
class File:
    def __init__(self, name: str, size_bytes: int):
        self.name = name
        self.size_bytes = size_bytes

    def __repr__(self):
        return f"File(name={self.name}, size={self.size_bytes}B)"

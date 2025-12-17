class File:
    def __init__(self, size_bytes: int, name: str = None):
        if size_bytes < 0:
            raise ValueError("size_bytes must be >= 0")
        self.size_bytes = size_bytes
        self.name = name or f"file_{size_bytes}"

    def __repr__(self):
        return f"File(name={self.name}, size={self.size_bytes})"


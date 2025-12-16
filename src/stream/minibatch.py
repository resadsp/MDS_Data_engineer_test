class MiniBatch:
    def __init__(self):
        self.messages: List = []

    def add(self, msg):
        self.messages.append(msg)

    def __len__(self):
        return len(self.messages)

    def __repr__(self):
        return f"MiniBatch({len(self.messages)} messages)"

from typing import List

class MiniBatch:
    def __init__(self):
        self.messages: List = []

    def add(self, msg):
        self.messages.append(msg)

    def __len__(self):
        return len(self.messages)

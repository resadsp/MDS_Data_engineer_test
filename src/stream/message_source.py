import time
from .message import Message

class MessageSource:
    def __init__(self, rate_per_minute: int):
        self.rate_per_minute = rate_per_minute
        self._callbacks = []

    def subscribe(self, callback):
        self._callbacks.append(callback)

    def _notify(self, msg):
        for cb in self._callbacks:
            cb(msg)

    def start(self):
        interval = 60 / self.rate_per_minute
        for i in range(5):
            self._notify(Message(f"msg_{i}"))
            time.sleep(interval)

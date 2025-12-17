import time

class Clock:
    @staticmethod
    def now() -> float:
        return time.time()

import time

class Clock:
    """
    Simple abstraction for current time, useful for testing.
    """

    @staticmethod
    def now() -> float:
        """
        Return current time in seconds since epoch.
        """
        return time.time()

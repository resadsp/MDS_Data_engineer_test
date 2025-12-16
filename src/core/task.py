from abc import ABC, abstractmethod

class Task(ABC):
    """
    Base abstraction for all tasks executed by the worker pool.
    """

    @abstractmethod
    def execute(self) -> None:
        """
        Execute the task logic.
        Concrete implementations must override this method.
        """
        pass

from abc import ABC, abstractmethod


class DataStorage(ABC):
    """An abstract class for a temporary SC2 data storage unit/container"""

    def __init__(self):
        self.data = []

    @abstractmethod
    def push(self) -> None:
        pass

    @abstractmethod
    def set_data(self) -> None:
        pass

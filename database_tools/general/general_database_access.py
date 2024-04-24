from abc import ABC, abstractmethod


class DataStorage(ABC):
    """
    An abstract class for a temporary data storage unit/container
    """

    def __init__(self) -> None:
        self._data = []

    @abstractmethod
    def push(self) -> None:
        pass

    @abstractmethod
    def set_data(self) -> None:
        pass

    def get_length(self) -> int:
        return len(self._data)

from abc import ABC, abstractmethod

class DataStorage(ABC):
    @abstractmethod
    def push(self) -> None:
        pass
    @abstractmethod
    def set_data(self) -> None:
        pass
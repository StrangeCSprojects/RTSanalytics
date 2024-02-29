from abc import ABC, abstractmethod

class Table(ABC):
    @abstractmethod
    def push(self) -> None:
        pass
    def set_data(self) -> None:
        pass
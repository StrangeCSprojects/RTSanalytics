from abc import ABC, abstractmethod

class Builds(ABC):
    @abstractmethod
    def determine_build(self) -> str:
        pass
    
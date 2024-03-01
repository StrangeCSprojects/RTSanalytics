from abc import ABC, abstractmethod
class Winrate(ABC):
    @abstractmethod
    def determine_winrate() -> int:
        pass
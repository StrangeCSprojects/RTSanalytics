from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def configure_report(self):
        pass
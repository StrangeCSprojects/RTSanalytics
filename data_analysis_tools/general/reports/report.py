from abc import ABC, abstractmethod

class Report(ABC):
    def __init__(self, data_retriever) -> None:
        self.data_retriever = data_retriever

    @abstractmethod
    def configure_report(self):
        pass
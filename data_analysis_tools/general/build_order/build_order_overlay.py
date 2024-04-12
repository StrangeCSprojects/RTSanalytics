from abc import ABC, abstractmethod
from database_tools.general.data_retriever import DataRetriever

class BuildOrderOverlay(ABC):
    def __init__(self, data_retriever:DataRetriever) -> None:
        super().__init__()
        self.data_retriever = data_retriever

    @abstractmethod
    def overlay_build(build_name:str) -> None:
        pass

    
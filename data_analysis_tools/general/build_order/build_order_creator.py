from database_tools.general.general_database import GeneralDB
from abc import ABC, abstractmethod

class BuildOrderCreator(ABC):
    
    @abstractmethod
    def create_build(self, build_file:str) -> None:
        pass
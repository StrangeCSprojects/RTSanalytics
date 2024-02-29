from abc import ABC, abstractmethod
from database_tools.general_database_access import Table

class Extractor(ABC):
    """
    Abstract class that extracts data from a group of replays, filters the data into
    table classes and inserts that data into a database.
    """
    def __init__(self, folder_path: str) -> None:
        super().__init__()
        self.folder_path = folder_path

    @abstractmethod
    def extract(self) -> dict:
        pass

    @abstractmethod
    def filter_into_tables(self, replay_container:dict) -> None:
        pass

    @abstractmethod
    def get_tables(self) -> list[Table]:
        pass

    def run(self) -> None:
        self.filter_into_tables(self.extract())
        self.batch_insert(self.get_tables())

    def batch_insert(self, table_list:list[Table]) -> None:
        for table in table_list:
            table.push()
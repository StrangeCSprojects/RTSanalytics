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
    def extract(self) -> None:
        pass

    @abstractmethod
    def filter_into_tables(self) -> None:
        pass

    def batch_insert(self, table_list:list[Table]) -> None:
        for table in table_list:
            table.push()
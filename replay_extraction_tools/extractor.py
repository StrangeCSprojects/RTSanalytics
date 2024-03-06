from abc import ABC, abstractmethod
from database_tools.general_database_access import DataStorage


class Extractor(ABC):
    """
    Abstract class that extracts data from a group of replays, filters the data into
    table classes and inserts that data into a database.
    """

    def __init__(self) -> None:
        self.folder_path = None

    @abstractmethod
    def extract(self) -> dict:
        pass

    @abstractmethod
    def filter_into_tables(self, replay_container: dict) -> None:
        pass

    @abstractmethod
    def build_order(self):
        pass

    @abstractmethod
    def _get_tables(self) -> list[DataStorage]:
        pass

    def run(self, folder_path: str) -> None:
        self.folder_path = folder_path
        self.filter_into_tables(self.extract())
        self._batch_insert(self._get_tables())

    def _batch_insert(self, table_list: list[DataStorage]) -> None:
        for table in table_list:
            table.push()

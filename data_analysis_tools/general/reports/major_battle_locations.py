from data_analysis_tools.general.reports.report import (
    Report,
)  # Base class for creating reports.
from database_tools.general.data_retriever import (
    DataRetriever,
)  # Class for retrieving data from the database.
from database_tools.general.general_database import (
    GeneralDB,
)  # General database interaction class.


class MajorBattleLocations(Report):
    def __init__(self, data_retriever: DataRetriever) -> None:
        super().__init__(data_retriever)

    def configure_report(self) -> list:
        return super().configure_report()


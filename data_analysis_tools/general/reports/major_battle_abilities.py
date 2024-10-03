from data_analysis_tools.general.reports.report import (
    Report,
)  # Base class for creating reports.
from database_tools.general.data_retriever import (
    DataRetriever,
)  # Class responsible for retrieving data from the database.
from database_tools.general.general_database import (
    GeneralDB,
)  # General database interaction class.


class MajorBattleAbilities(Report):
    """
    A class that generates reports on the use of abilities during major battles based on unit data.
    Inherits from the Report class.
    """

    def __init__(
        self,
        data_retriever: DataRetriever,
    ) -> None:
        """
        Initialize the MajorBattleAbilities class with a data retriever.

        :param data_retriever: An instance of DataRetriever for accessing unit ability usage data.
        """
        super().__init__(data_retriever)
        self.data_retriever = (
            data_retriever  # Data retriever instance for accessing ability usage data.
        )

    def configure_report(self) -> dict:
        """
        Configure the report by retrieving unit ability usage data within a given time range.

        :return: A dictionary containing the abilities used by both players during the battle.
                 The keys are 'player_one' and 'player_two', and the values are lists of abilities used.
                 Example:
                 {
                     'player_one': ['Psionic Storm', 'Force Field'],
                     'player_two': ['Stimpack', 'Medivac Heal']
                 }
        """
        return self.data_retriever.get_abilities_by_time_range()

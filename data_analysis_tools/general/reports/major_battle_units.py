from data_analysis_tools.general.reports.report import (
    Report,
)  # Base class for creating reports.
from database_tools.general.data_retriever import (
    DataRetriever,
)  # Class responsible for retrieving data from the database.
from database_tools.general.general_database import (
    GeneralDB,
)  # General database interaction class.


class MajorBattleUnits(Report):
    """
    A class that generates reports on the location of major battles based on unit data.
    Inherits from the Report class.
    """

    def __init__(
        self,
        data_retriever: DataRetriever,
        time_of_battle: tuple[int, int],
        location: tuple[int, int],
    ) -> None:
        """
        Initialize the MajorBattleUnits class with a data retriever, time of battle, and location.

        :param data_retriever: An instance of DataRetriever for accessing unit death location data.
        :param time_of_battle: A tuple (start_time, end_time) representing the time range of the battle (in-game time).
        :param location: A tuple (center_x, center_y, radius) representing the center and radius of the circle
                         that defines the battle's location on the map.
        """
        super().__init__(data_retriever)
        self.time = time_of_battle
        self.loc = location
        self.data_retriever = data_retriever

    def configure_report(self) -> list:
        """
        Configure the report by retrieving unit data based on the time and location of the battle.

        :return: A list of unit data retrieved based on the battle's location and time.
        """
        return self.data_retriever.get_units_by_location_and_time()

from data_analysis_tools.general.analyzer import (
    Analyzer,
)  # Base class for analysis tools.
from database_tools.general.data_retriever import DataRetriever
from database_tools.sc2.sc2_replay_data_retriever import (
    SC2ReplayDataRetriever,
)  # Specific data retriever for SC2 replay data.
from data_analysis_tools.general.reports.major_battle_timestamps import MajorBattleTimeStamps
from data_analysis_tools.general.reports.major_battle_location import MajorBattleLocations
import logging  # Standard Python module for logging
from config.sc2_logging_config import (
    setup_logging,
)  # Function to set up logging for SC2 analysis


class SC2MajorBattlesAnalyzer(Analyzer):
    """
    An analyzer class to handle the analysis of major battles in StarCraft 2 replays.
    Inherits from the base Analyzer class.
    """

    def __init__(self, data_retriever: DataRetriever) -> None:
        """
        Initializes the SC2MajorBattlesAnalyzer with a data retriever.

        :param data_retriever: An instance of DataRetriever to fetch data for analysis.
        """
        super().__init__(data_retriever)  # Initialize the parent Analyzer class
        self.sc2_major_battle_timestamps = MajorBattleTimeStamps(
            self.data_retriever
        )  # Create a report for major battles

        self.sc2_major_battle_locations = MajorBattleLocations(
            self.data_retriever
        )  # Create a report for major battles


    def major_battle_timestamps(self) -> list:
        """
        Generate and return a report of major battles.

        :return: Return the list of major battle timestamps
        """
        return self.sc2_major_battle_timestamps.configure_report()

    def major_battle_locations(self) -> list:
        return self.sc2_major_battle_locations.configure_report()
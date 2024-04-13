from abc import ABC, abstractmethod
from data_analysis_tools.general.analyzer import Analyzer


class GetWinratesRace(ABC):
    # Define the analyzer attribute
    analyzer: Analyzer

    @abstractmethod
    def get_winrates_race(cls):
        pass

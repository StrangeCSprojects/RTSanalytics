from data_analysis_tools.general.reports.report import (
    Report,
)  # Base class for creating reports.
from database_tools.general.data_retriever import (
    DataRetriever,
)  # Class for retrieving data from the database.
from database_tools.general.general_database import (
    GeneralDB,
)  # General database interaction class.


class MajorBattleLocation(Report):
    def __init__(self, data_retriever: DataRetriever, time_of_battle: tuple[int,int]) -> None:
        super().__init__(data_retriever)
        battle_start = time_of_battle[0]
        battle_end = time_of_battle[1]
        self.start_unit_locations = self.data_retriever.get_all_locations_at_time(battle_start)
        self.end_unit_locations = self.data_retriever.get_all_locations_at_time(battle_end)

    def configure_report(self) -> list:
        pass

    def __find_battle_start_location__(self):
        pass

    def __find_battle_end_location__(self):
        pass

    def __dbscan__(self):
        pass

    def __least_fitting_squares__(self):
        pass


    

    



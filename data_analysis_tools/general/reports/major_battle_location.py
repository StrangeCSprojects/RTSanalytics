from data_analysis_tools.general.reports.report import (
    Report,
)  # Base class for creating reports.
from database_tools.general.data_retriever import (
    DataRetriever,
)  # Class for retrieving data from the database.
from database_tools.general.general_database import (
    GeneralDB,
)  # General database interaction class.

import numpy as np
from sklearn import metrics
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull


class MajorBattleLocation(Report):
    def __init__(self, data_retriever: DataRetriever, time_of_battle: tuple[int,int]) -> None:
        super().__init__(data_retriever)
        battle_start = time_of_battle[0]
        battle_end = time_of_battle[1]
        self.start_unit_locations = self.data_retriever.get_unit_death_locations_at_time(battle_start)
        self.end_unit_locations = self.data_retriever.get_unit_death_locations_at_time(battle_end)

    def configure_report(self) -> list:
        start_loc = self.__find_battle_start_location__()
        end_loc = self.__find_battle_end_location__()
        return (start_loc, end_loc)

    def __find_battle_start_location__(self):
        dbscan = self.__dbscan__(self.battle_start)

    def __find_battle_end_location__(self):
        dbscan = self.__dbscan__(self.battle_end)

    def __dbscan__(self, list_of_coord):
        return DBSCAN(eps=10, min_samples=10).fit(list_of_coord)

    def find_circle_coord(self, points):
        hull = ConvexHull(points)
        
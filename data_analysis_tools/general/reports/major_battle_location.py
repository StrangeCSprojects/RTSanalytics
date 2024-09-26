from data_analysis_tools.general.reports.report import (
    Report,
)  # Base class for creating reports.
from database_tools.general.data_retriever import (
    DataRetriever,
)  # Class for retrieving data from the database.
from database_tools.general.general_database import (
    GeneralDB,
)  # General database interaction class.

import numpy as np  # Import NumPy for numerical computations.
from sklearn import (
    metrics,
)  # Import metrics from Scikit-learn for evaluation purposes (not used in this code).
from sklearn.cluster import (
    DBSCAN,
)  # Import DBSCAN clustering algorithm from Scikit-learn.
import matplotlib.pyplot as plt  # Import Matplotlib for plotting (not used in this code).
from scipy.spatial import (
    ConvexHull,
)  # Import ConvexHull for creating convex hulls around points.


class MajorBattleLocation(Report):
    """
    A class to generate reports on the location of major battles based on unit death data.
    Inherits from the Report class.
    """

    def __init__(
        self, data_retriever: DataRetriever, time_of_battle: tuple[int, int]
    ) -> None:
        """
        Initialize the MajorBattleLocation with a data retriever and time of battle.

        :param data_retriever: An instance of DataRetriever to retrieve unit death location data.
        :param time_of_battle: A tuple containing the start and end time of the battle (in-game time).
        """
        super().__init__(data_retriever)
        battle_start = time_of_battle[0]
        battle_end = time_of_battle[1]

        # Retrieve unit death locations at the start and end of the battle.
        self.start_unit_locations = (
            self.data_retriever.get_unit_death_locations_at_time(battle_start)
        )
        self.end_unit_locations = self.data_retriever.get_unit_death_locations_at_time(
            battle_end
        )

    def configure_report(self) -> tuple[int, int]:
        """
        Configure the report to determine the location of the major battle.

        :return: A tuple containing the estimated center and radius of the major battle location.
        """
        # Call helper function to determine the battle location.
        battle_loc = self.__find_battle_location__(
            self.start_unit_locations, self.end_unit_locations
        )
        return battle_loc

    def __find_battle_location__(self, start: list, end: list) -> tuple[int, int]:
        """
        Private method to calculate the battle location based on unit death locations.

        :param start: List of unit death locations at the start of the battle.
        :param end: List of unit death locations at the end of the battle.
        :return: A tuple containing the estimated center and radius of the battle location.
        """
        # Combine the unit death locations from both the start and end of the battle.
        all_unit_loc = start + end

        # Use DBSCAN clustering to filter noise and group locations.
        dbscan = DBSCAN(eps=10, min_samples=10).fit(all_unit_loc)
        labels = dbscan.labels_  # Cluster labels from DBSCAN.

        # Select the points that are not labeled as noise (-1 represents noise).
        points = all_unit_loc[labels != -1]

        # Create a convex hull around the points to determine the battle area.
        hull = ConvexHull(points)

        # Extract the points that form the vertices of the convex hull.
        hull_points = hull[points.vertices]

        # Calculate the center of the battle area as the mean of the hull points.
        center = np.mean(hull_points, axis=0)

        # Calculate the radius as the maximum distance from the center to any hull point.
        radius = np.max(np.linalg.norm(hull_points - center, axis=1))

        return (center, radius)

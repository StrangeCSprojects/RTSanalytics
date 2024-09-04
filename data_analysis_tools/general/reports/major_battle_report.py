from data_analysis_tools.general.reports.report import (
    Report,
)  # Base class for creating reports.
from database_tools.general.data_retriever import (
    DataRetriever,
)  # Class for retrieving data from the database.
from database_tools.general.general_database import (
    GeneralDB,
)  # General database interaction class.


class MajorBattleReport(Report):
    """
    A class to generate a report on major battles based on unit death data.
    Inherits from the Report class.
    """

    def __init__(self, data_retriever: DataRetriever) -> None:
        """
        Initialize the MajorBattleReport with a data retriever instance.

        :param data_retriever: An instance of DataRetriever to retrieve unit death data.
        """
        self.data_retriever = data_retriever

    def configure_report(self) -> list:
        """
        Configure the report to identify major battles.

        A major battle is identified when the total resource value of unit deaths within a detection window
        exceeds a certain threshold.

        :return: A list of tuples, where each tuple contains the start and end timestamps of a major battle.
        """
        major_battle_timestamps = (
            []
        )  # List to store start and end timestamps of identified major battles.
        resource_total = 0  # Total resource value of units currently in the battle.
        detection_window = 15  # Time window in seconds to detect if deaths are part of the same battle.
        resource_threshold = (
            5000  # Threshold of resource value to qualify as a major battle.
        )
        units_in_battle = (
            []
        )  # List to store units considered to be in the current battle.
        last_death_time = 0  # Timestamp of the last unit death.

        # Retrieve all unit death data from the data retriever
        all_unit_deaths = self.data_retriever.get_all_unit_deaths()

        # Iterate over each unit death record
        for unit in all_unit_deaths:
            time_of_death = unit[1]  # Extract the time of death from the unit record.
            resource_value = unit[
                2
            ]  # Extract the resource value associated with the unit.

            # Check if this death is within the detection window to be considered part of the current battle
            if (
                last_death_time == 0
                or time_of_death - last_death_time < detection_window
            ):
                units_in_battle.append(unit)  # Add the unit to the current battle.
                resource_total += (
                    resource_value  # Add the unit's resource value to the total.
                )
                last_death_time = time_of_death  # Update the last death time.
            elif resource_total >= resource_threshold:
                # If the total resource value exceeds the threshold, mark the battle timestamps
                battle_start = units_in_battle[0][1]  # Start time of the battle.
                battle_end = units_in_battle[-1][1]  # End time of the battle.
                timestamp = (battle_start, battle_end)
                major_battle_timestamps.append(
                    timestamp
                )  # Add the battle timestamps to the report.

                # Reset for the next potential battle
                resource_total = resource_value
                units_in_battle = [unit]
                last_death_time = time_of_death
            else:
                # Reset if no major battle is detected
                resource_total = 0
                units_in_battle = []
                last_death_time = 0

        # Check one more time if the last set of unit deaths constitutes a major battle
        if resource_total >= resource_threshold:
            # If the total resource value exceeds the threshold, mark the battle timestamps
            battle_start = units_in_battle[0][1]  # Start time of the battle.
            battle_end = units_in_battle[-1][1]  # End time of the battle.
            timestamp = (battle_start, battle_end)
            major_battle_timestamps.append(
                timestamp
            )  # Add the battle timestamps to the report.

        return major_battle_timestamps  # Return the list of major battle timestamps.

import os
import sc2reader
from database_tools.general.general_database_access import DataStorage
from replay_extraction_tools.General.extractor import Extractor
import logging


class SC2MajorBattlesExtractor(Extractor):
    def __init__(self) -> None:
        """
        Initialize the SC2MajorBattlesExtractor with base class and unit death data storage.
        """
        super().__init__()
        self._unit_death_data = UnitDeathDataStorage()

    def extract(self) -> dict:
        """
        Extract data from a group of replays and return a dictionary of replay data.

        Returns:
        A dictionary where keys are replay identifiers and values are the corresponding replay data.
        """
        replay_container = {}
        replay_counter = 0

        # Getting replays from folder
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path) and file_path.endswith(".SC2Replay"):
                # Filling replay dictionary
                replay_counter += 1

                # Check file loads properly
                try:
                    replay = sc2reader.load_replay(file_path, load_map=True)
                except Exception:
                    logging.warning(f"File: {file_path} - File failed to load")

                replay_container[replay_counter] = replay

            else:
                # Log warning if file is not found or isn't of type .SC2Replay
                logging.warning("File not found or File isn't of type .SC2Replay")

        return replay_container

    def filter_into_tables(self, replay_container: dict) -> None:
        """
        Filter and process the replay data, extracting significant battle events.

        Parameters:
        replay_container: A dictionary containing replays to be processed.
        """
        # Should only have one replay in folder
        replay = replay_container[0]

        worthless_units = ["Larva", "Egg", "Broodling", "Locust", "Mule"]

        # Get all the "Unit Died" events, ignoring units that have no resource value
        dead_units = [
            event
            for event in replay.events
            if event.name == "UnitDiedEvent"
            and not any(
                worthless_unit in str(event.unit) for worthless_unit in worthless_units
            )
        ]

        # Extract information required from the units that died in the replay
        for unit in dead_units:
            unit_id = self._get_unit_id()
            death_timer = self._get_death_timer(unit)
            resource_count = self._get_resource_count(unit)

            unit_deaths_record = (unit_id, death_timer, resource_count)

            self._unit_death_data.set_data(unit_deaths_record)

    def _get_tables(self) -> list[DataStorage]:
        """
        Retrieve the list of data storage tables used in the extractor.

        Returns:
        A list containing the data storage tables used by the extractor, specifically the unit death data table.
        """
        return [self._unit_death_data]

    def run(self, folder_path: str) -> None:
        """
        Execute the extraction process on a given folder path.

        Parameters:
        folder_path: The path to the folder containing the replay files to be processed.
        """
        return super().run(folder_path)

    def _batch_insert(self, table_list: list[DataStorage]) -> None:
        """
        Insert the processed data into the appropriate tables in batches.

        Parameters:
        table_list: A list of data storage tables where the data should be inserted.
        """
        return super()._batch_insert(table_list)

    def _get_unit_id(self) -> int:
        """
        Generate a unique identifier for a unit.

        Returns:
        An integer representing the unique ID of a unit.
        """
        return SC2MajorBattlesDB._create_unit_id()

    def _get_death_timer(self, unit) -> int:
        """
        Retrieve the time at which a unit died during the replay.

        Parameters:
        unit: The unit object for which the death time is being retrieved.

        Returns:
        An integer representing the second in the game when the unit died.
        """
        return unit.second

    def _get_resource_count(self, unit) -> int:
        """
        Retrieve the resource value of a unit that died.

        Parameters:
        unit: The unit object for which the resource value is being retrieved.

        Returns:
        An integer representing the resource cost of the unit.
        """
        unit_values = {
            "Banshee": 250,
            "Battlecruiser": 700,
            "Cyclone": 175,
            "Ghost": 275,
            "Hellbat": 100,
            "Hellion": 100,
            "Liberator": 275,
            "Marauder": 125,
            "Marine": 50,
            "Medivac": 200,
            "Raven": 250,
            "Reaper": 100,
            "SCV": 50,
            "Siege Tank": 275,
            "Thor": 500,
            "Viking": 225,
            "Widow Mine": 100,
            "Adept": 100,
            "Archon": 400,
            "Carrier": 600,
            "Colossus": 500,
            "Dark Templar": 250,
            "High Templar": 200,
            "Immortal": 375,
            "Interceptor": 15,
            "Mothership": 600,
            "Observer": 100,
            "Oracle": 300,
            "Phoenix": 250,
            "Probe": 50,
            "Sentry": 150,
            "Stalker": 175,
            "Tempest": 425,
            "Void Ray": 400,
            "Warp Prism": 250,
            "Zealot": 100,
            "Baneling": 50,
            "Brood Lord": 550,
            "Corruptor": 250,
            "Drone": 50,
            "Hydralisk": 150,
            "Infestor": 250,
            "Lurker": 300,
            "Mutalisk": 200,
            "Overlord": 100,
            "Overseer": 200,
            "Roach": 100,
            "Swarm Host": 275,
            "Ultralisk": 475,
            "Ventral Sacs Overlord": 150,
            "Viper": 300,
            "Zergling": 25,
        }
        if unit in unit_values:
            return unit_values[unit]

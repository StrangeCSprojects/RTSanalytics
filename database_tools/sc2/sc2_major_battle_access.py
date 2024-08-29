from json import (
    dumps,
)  # Import the dumps function for potential future use in JSON serialization.
from database_tools.general.general_database_access import (
    DataStorage,
)  # Import base class for data storage operations.
from database_tools.sc2.sc2_major_battle_database import (
    SC2MajorBattleDB,
)  # Import SC2 database class for managing major battle data.


class UnitDeathDataStorage(DataStorage):
    """
    A class for managing unit death data storage for StarCraft II major battles.
    This class provides methods to set data and push it to the SC2MajorBattleDB.
    """

    def push(self) -> None:
        """
        Pushes the current unit death data stored in this instance to the SC2MajorBattleDB.
        """
        SC2MajorBattleDB.add_unit_deaths(
            self._data
        )  # Add all stored unit deaths to the database.

    def set_data(self, new_record:tuple[int,int,int]) -> None:
        """
        Adds a new unit death record to the internal data list.

        :param new_record: A tuple containing the unit death data (id, time, resource).
        """
        id, time, resource = (
            new_record  # Unpack the new record tuple into individual components.
        )
        self._data.append(
            (id, time, resource)
        )  # Append the new record to the internal data list.

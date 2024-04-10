from json import dumps
from database_tools.general.general_database_access import DataStorage
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB

# Implement and add the new database later


class BuildOrderDataStorage(DataStorage):
    """
    Contains data for the build order table
    """

    def push(self) -> None:
        SC2BuildOrderDB.add_build_order(self._data)

    def set_data(self, new_record) -> None:
        name, race, commands = new_record
        serialized_commands = dumps(commands)
        self._data.append((name, race, serialized_commands))

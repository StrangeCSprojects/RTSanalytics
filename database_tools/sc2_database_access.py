from database_tools.general_database_access import DataStorage
from database_tools.sc2_database import SC2_DB


class CommandDataStorage(DataStorage):
    """
    Contains data for the Commands table in a SC2 game
    """

    def push(self) -> None:
        # PERFORM ANY ADDITIONAL SECURITY CHECKS BEFORE PUSHING
        SC2_DB.add_commands(self._data)

    def set_data(self, new_record) -> None:
        pass


class PlayDataStorage(DataStorage):
    """
    Contains data for the Play table
    """

    def push(self) -> None:
        pass

    def set_data(self, new_record) -> None:
        self._data.append(new_record)


class PlayerDataStorage(DataStorage):
    """
    Contains data for the Player table
    """
    
    def __init__(self):
        """Data container is a dictionary"""
        self.data = {}

    def push(self) -> None:
        pass

    def set_data(self, new_record) -> None:
        command_id = new_record[0]
        commands_list = new_record[1]
        self.data[command_id] = commands_list


class IssuesDataStorage(DataStorage):
    """
    Contains data for the Issues table
    """

    def push(self) -> None:
        pass

    def set_data(self, new_record) -> None:
        self._data.append(new_record)


class GameDataStorage(DataStorage):
    """
    Contains data for the Game table
    """

    def push(self) -> None:
        """Push the game data to the SC2 database"""
        SC2_DB.add_games(self._data)

    def set_data(self, new_game_data) -> None:
        """Store relevant game data in a tuple and add to data list"""
        self._data.append(new_game_data)

from database_tools.general_database_access import DataStorage
from database_tools.sc2_database import SC2_DB


class CommandDataStorage(DataStorage):
    """
    Contains data for the Commands table in a SC2 game
    """

    def push(self) -> None:
        # PERFORM ANY ADDITIONAL SECURITY CHECKS BEFORE PUSHING
        SC2_DB.add_commands(self.data)

    def set_data(self) -> None:
        pass


class PlayDataStorage(DataStorage):
    """
    Contains data for the Play table
    """

    def push(self) -> None:
        pass

    def set_data(self) -> None:
        pass


class PlayerDataStorage(DataStorage):
    """
    Contains data for the Player table
    """

    def push(self) -> None:
        pass

    def set_data(self) -> None:
        pass


class IssuesDataStorage(DataStorage):
    """
    Contains data for the Issues table
    """

    def push(self) -> None:
        pass

    def set_data(self) -> None:
        pass


class GameDataStorage(DataStorage):
    """
    Contains data for the Game table
    """

    def push(self) -> None:
        """Push the game data to the SC2 database"""
        SC2_DB.add_games(self.data)

    def set_data(self, new_game_data) -> None:
        """Store relevant game data in a tuple and add to data list"""
        self.data.append(new_game_data)

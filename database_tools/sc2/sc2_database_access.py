from json import dumps
from database_tools.general.general_database_access import DataStorage
from database_tools.sc2.sc2_database import SC2_DB


class PlayDataStorage(DataStorage):
    """
    Contains data for the Play table
    """

    def push(self) -> None:
        SC2_DB.add_plays(self._data)

    def set_data(self, new_record) -> None:
        game_id, player_id, race, is_winner, commands = new_record
        serialized_commands = dumps(commands)
        self._data.append((game_id, player_id, race, is_winner, serialized_commands))


class PlayerDataStorage(DataStorage):
    """
    Contains data to be pushed to the Player table
    """

    def push(self) -> None:
        SC2_DB.add_players(self._data)

    def set_data(self, new_record) -> None:
        self._data.append(new_record)

    def _get_player_from_storage(self, name: str) -> dict:
        p_query = [(p_id, p_name) for p_id, p_name in self._data if p_name == name]
        if p_query:
            p_id, p_name = p_query[0]
            return {"player_id": p_id, "p_name": p_name}
        return None


class GameDataStorage(DataStorage):
    """
    Contains data for the Game table
    """

    def push(self) -> None:
        SC2_DB.add_games(self._data)

    def set_data(self, new_record) -> None:
        self._data.append(new_record)

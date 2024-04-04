from json import loads
from database_tools.general.data_retriever import DataRetriever
from database_tools.sc2.sc2_database import SC2ReplayDB


class SC2DataRetriever(DataRetriever):
    """
    A subclass of DataRetriever tailored for retrieving StarCraft II (SC2) related data.
    It provides methods for fetching specific data about players, plays, games, issues, and commands,
    as well as methods for fetching all records of these types from the database.

    This class leverages inheritance to extend or modify the functionality of the DataRetriever
    class to suit the specific needs of accessing and analyzing StarCraft II data.
    """

    def __init__(self, database:SC2ReplayDB) -> None:
        """
        Initialize the SC2DataRetriever with a database connection or configuration.

        :param database: The database connection or configuration to be used for data retrieval.
        """
        super().__init__(
            database
        )  # Calls the initializer of the superclass (DataRetriever)

    def get_player(self, player_id:int):
        """
        Retrieve a single player's data from the database.
        """
        pass

    def get_play(self, game_id:int, player_id:int):
        """
        Retrieve a single play's data from the database.
        """
        return self.database.get_play(game_id, player_id)

    def get_game(self, game_id:int):
        """
        Retrieve a single game's data from the database.
        """
        pass

    def get_commands(self, game_id:int, player_id:int):
        """
        Retrieve data about a single command from the database.
        """
        play = self.get_play(game_id, player_id)
        serialized_commands = play[2]
        temp_result = loads(serialized_commands)

        # turning list of lists, into a list of tuples
        result = [(tuple(inner_list[0]), inner_list[1]) for inner_list in temp_result]

        return result

    def get_all_players(self):
        """
        Retrieve data for all players from the database.
        This method is to be implemented to specify how to fetch data for all players.
        """
        return self.database.get_all_players()

    def get_all_plays(self):
        """
        Retrieve data for all plays from the database.
        """
        pass

    def get_all_games(self):
        """
        Retrieve data for all games from the database.
        """
        return self.database.get_all_games()

    def get_all_commands(self):
        """
        Retrieve data for all commands from the database.
        """
        pass

    def get_players_in_game(self, game_id:int):
        """
        Retrieve data for all players in a specific game
        """
        return self.database.get_players_in_game(game_id)

    def get_winner(self, game_id: int, player_id: int):
        """
        Returns True or False depending on whether or not
        a specific player won a specific sc2 game
        """
        return self.get_play(game_id, player_id)[1]

    def get_player_race(self, game_id: int, player_id: int):
        """
        Retrieves race of a player in a specific game
        """
        return self.get_play(game_id, player_id)[0]

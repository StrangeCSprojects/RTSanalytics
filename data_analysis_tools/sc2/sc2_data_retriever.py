from data_analysis_tools.general.data_retriever import DataRetriever


class SC2DataRetriever(DataRetriever):
    """
    A subclass of DataRetriever tailored for retrieving StarCraft II (SC2) related data.
    It provides methods for fetching specific data about players, plays, games, issues, and commands,
    as well as methods for fetching all records of these types from the database.

    This class leverages inheritance to extend or modify the functionality of the DataRetriever
    class to suit the specific needs of accessing and analyzing StarCraft II data.
    """

    def __init__(self, database) -> None:
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
        pass

    def get_game(self):
        """
        Retrieve a single game's data from the database.
        """
        pass

    def get_issues(self):
        """
        Retrieve data about a single issue from the database.
        """
        pass

    def get_commands(self):
        """
        Retrieve data about a single command from the database.
        """
        pass

    def get_all_players(self):
        """
        Retrieve data for all players from the database.
        This method is to be implemented to specify how to fetch data for all players.
        """
        pass

    def get_all_plays(self):
        """
        Retrieve data for all plays from the database.
        """
        pass

    def get_all_games(self):
        """
        Retrieve data for all games from the database.
        """
        pass

    def get_all_issues(self):
        """
        Retrieve data for all issues from the database.
        """
        pass

    def get_all_commands(self):
        """
        Retrieve data for all commands from the database.
        """
        pass

    def get_players_in_game(self, game_id:int) -> tuple[int,int]:
        pass
    
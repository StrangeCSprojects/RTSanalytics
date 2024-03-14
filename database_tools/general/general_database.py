from abc import ABC, abstractmethod

class General_DB(ABC):
    """
    A class for interacting with the SC2 database. Concrete implementations of the General_DB class
    must provide a method of storing data in a database system like SQLAlchemy, SQLite, or any other systems
    compatible with the General_DB interface.
    """

    @abstractmethod
    def init(self, db_name):
        """Initializes database connection."""
        pass

    @abstractmethod
    def add_games(self, game_list):
        """Adds games to the database."""
        pass

    @abstractmethod
    def add_players(self, player_list):
        """Adds players to the database."""
        pass

    @abstractmethod
    def add_plays(self, play_list):
        """Adds plays to the database."""
        pass

    @abstractmethod
    def get_player_by_name(self, name: str) -> dict:
        """Retrieves a player by name."""
        pass

    @abstractmethod
    def get_player_by_id(self, id: int):
        """Retrieves a player by ID."""
        pass

    @abstractmethod
    def get_players_in_game(self, game_id: int):
        """Retrieves players in a specific game."""
        pass

    @abstractmethod
    def get_play(self, game_id: int, player_id: int):
        """Retrieves a play by game ID and player ID."""
        pass

    @abstractmethod
    def get_all_plays(self):
        """Retrieves all plays from the database."""
        pass

    @abstractmethod
    def get_all_players(self):
        """Retrieves all players from the database."""
        pass

    @abstractmethod
    def get_all_games(self):
        """Retrieves all games from the database."""
        pass

    @abstractmethod
    def _create_game_id(self) -> int:
        """Creates a game ID."""
        pass

    @abstractmethod
    def _create_player_id(self) -> int:
        """Creates a player ID."""
        pass

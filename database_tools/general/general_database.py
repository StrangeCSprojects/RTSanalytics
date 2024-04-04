from abc import ABC, abstractmethod

class GeneralDB(ABC):
    """
    A class for interacting with the SC2 database. Concrete implementations of the General_DB class
    must provide a method of storing data in a database system like SQLAlchemy, SQLite, or any other systems
    compatible with the General_DB interface.
    """

    @abstractmethod
    def init(cls, db_name):
        """Initializes database connection."""
        pass

    @abstractmethod
    def add_games(cls, game_list):
        """Adds games to the database."""
        pass

    @abstractmethod
    def add_players(cls, player_list):
        """Adds players to the database."""
        pass

    @abstractmethod
    def add_plays(cls, play_list):
        """Adds plays to the database."""
        pass

    @abstractmethod
    def get_player_by_name(cls, name: str) -> dict:
        """Retrieves a player by name."""
        pass

    @abstractmethod
    def get_player_by_id(cls, id: int):
        """Retrieves a player by ID."""
        pass

    @abstractmethod
    def get_players_in_game(cls, game_id: int):
        """Retrieves players in a specific game."""
        pass

    @abstractmethod
    def get_play(cls, game_id: int, player_id: int):
        """Retrieves a play by game ID and player ID."""
        pass

    @abstractmethod
    def get_all_plays(cls):
        """Retrieves all plays from the database."""
        pass

    @abstractmethod
    def get_all_players(cls):
        """Retrieves all players from the database."""
        pass

    @abstractmethod
    def get_all_games(cls):
        """Retrieves all games from the database."""
        pass

    @abstractmethod
    def _create_game_id(cls) -> int:
        """Creates a game ID."""
        pass

    @abstractmethod
    def _create_player_id(cls) -> int:
        """Creates a player ID."""
        pass

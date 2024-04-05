# Import any needed modules
from json import loads
from sqlalchemy import create_engine
from sqlalchemy.orm import ClassManager, sessionmaker
from database_tools.general.general_database import GeneralDB
from database_tools.sc2.entities.sc2_db_entities import (
    Base,
    Game,
    Play,
    Player,
)


class SC2ReplayDB(GeneralDB):
    """
    A class for interacting with the SC2 database
    """
    engine = None
    Session = None
        # ID initialization

    @classmethod
    def init(cls, db_name):
        """
        Initializes database connection
        """
        # Establish connection to the database file
        cls.engine = create_engine(f"sqlite:///database_tools/data/{db_name}.db")
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls._game_id_count = 0
        cls._player_id_count = 0


    @classmethod
    def add_games(cls, game_list):
        with cls.Session() as session:
            for game in game_list:
                id = game[0]
                game_map = game[1]
                game_mode = game[2]
                existing_game = session.query(Game).filter_by(game_id=id).first()
                if existing_game:
                    continue
                game = Game(
                    game_id=id,
                    map=game_map,
                    mode=game_mode,
                )
                session.add(game)
            session.commit()

    @classmethod
    def add_players(cls, player_list):
        with cls.Session() as session:
            for player_info in player_list:
                id = player_info[0]
                name = player_info[1]
                existing_player = session.query(Player).filter_by(player_id=id).first()
                if existing_player:
                    continue
                player = Player(player_id=id, name=name)
                session.add(player)
            session.commit()

    @classmethod
    def add_plays(cls, play_list):
        with cls.Session() as session:
            for play_info in play_list:
                game_id, player_id, race, is_winner, commands = play_info
                existing_play = (
                    session.query(Play)
                    .filter_by(game_id=game_id)
                    .filter_by(player_id=player_id)
                    .first()
                )
                if existing_play:
                    continue
                play = Play(
                    game_id=game_id,
                    player_id=player_id,
                    race=race,
                    winner=is_winner,
                    commands=commands,
                )
                session.add(play)
            session.commit()

    @classmethod
    def get_player_by_name(cls, name: str) -> dict:
        with cls.Session() as session:
            player = session.query(Player).filter_by(name=name).first()
            if player:
                return (player.player_id, player.name)
            else:
                return None

    @classmethod
    def get_player_by_id(cls, id: int):
        with cls.Session() as session:
            player = session.query(Player).filter_by(player_id=id).first()
            if player:
                return (player.player_id, player.name)
            else:
                return None

    @classmethod
    def get_players_in_game(cls, game_id: int):
        with cls.Session() as session:
            plays = session.query(Play).filter_by(game_id=game_id).all()
            players = tuple(cls.get_player_by_id(play.player_id) for play in plays)
            return players

    @classmethod
    def get_play(cls, game_id: int, player_id: int):
        with cls.Session() as session:
            play = (
                session.query(Play)
                .filter_by(game_id=game_id)
                .filter_by(player_id=player_id)
                .first()
            )
            return (play.race, play.winner, play.commands)

    @classmethod
    def get_all_plays(cls):
        with cls.Session() as session:
            plays = tuple(
                (play.game_id, play.player_id, play.race, play.winner, play.commands)
                for play in session.query(Play).all()
            )
            return plays

    @classmethod
    def get_all_players(cls):
        with cls.Session() as session:
            players = tuple(
                (player.player_id, player.name)
                for player in session.query(Player).all()
            )
            return players

    @classmethod
    def get_all_games(cls):
        with cls.Session() as session:
            games = tuple(
                (game.game_id, game.map, game.mode)
                for game in session.query(Game).all()
            )
            return games

    @classmethod
    def _create_game_id(cls) -> int:
        """Increment and return game id"""
        cls._game_id_count += 1
        return cls._game_id_count

    @classmethod
    def _create_player_id(cls) -> int:
        """Increment and return player id"""
        cls._player_id_count += 1
        return cls._player_id_count

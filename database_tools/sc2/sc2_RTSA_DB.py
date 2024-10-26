# Import any needed modules
from sqlalchemy import create_engine
from sqlalchemy.orm import ClassManager, sessionmaker, strategies, declarative_base
from database_tools.general.general_database import GeneralDB
from database_tools.sc2.entities.sc2_replay_entities import Game, Player, Play
from database_tools.sc2.entities.sc2_build_order_entities import BuildTemplate
from database_tools.sc2.entities.sc2_major_battle_entities import UnitDeath
import os
import configparser
import psycopg2
import logging


class SC2RTSADB(GeneralDB):
    """
    A singleton class acting as an interface to the RTS Analytics database for StarCraft II.
    This class is designed to manage the database operations related to StarCraft II
    build orders, game replays, and major battles.
    """

    @classmethod
    def init(cls):
        """
        This method sets up the PostgreSQL engine and sessionmaker for interacting with the database.

        NOTE: You must have a "config.ini" file in the current directory.
            (see README.md for more information)
        """
        
        # First get the path to the config file dynamically
        current_directory = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_directory, 'config.ini')

        # Load the config file
        config = configparser.ConfigParser()
        config.read(config_path)

        # Retrieve credentials from the config file
        username = config['database']['username']
        password = config['database']['password']
        host = config['database']['host']
        port = config['database']['port']
        database = config['database']['database']

        # Create an engine that stores data in the specified PostgreSQL database
        cls.engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")
        
        # Create a configured "Session" class bound to the database engine
        cls.Session = sessionmaker(bind=cls.engine)

        # Create all tables in the database (if not already existing) based on metadata.
        declarative_base().metadata.create_all(cls.engine)

        # Initialize a counter for build order IDs
        cls._build_order_id_count = 0 # TODO: MAY NOT NEED TO DO THIS NOW THAT WE HAVE POSTGRES

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
    def add_unit_deaths(cls, unit_death_list: list[tuple[int, int, int]]) -> None:
        """
        Adds multiple unit deaths to the database from a list of unit deaths.

        :param unit_death_list: A list of tuples, where each tuple contains unit death details (id, time, resource).
        """
        with cls.Session() as session:
            for unit_death in unit_death_list:
                # Unpack the unit death tuple into its components.
                id, time, resource = unit_death

                # Create a new UnitDeath instance for the new unit death.
                unit_death = UnitDeath(id=id, time=time, resource=resource)
                # Add the new unit death to the session.
                session.add(unit_death)
            # Commit all the pending unit death additions to the database.
            session.commit()

    @classmethod
    def add_build_templates(cls, build_templates):
        """
        Adds multiple build templates to the database from a list of build orders.
        Each template in the list is checked for existence before addition to prevent duplicates.
        """
        with cls.Session() as session:
            for template in build_templates:
                # Decompose the tuple into its components.
                build_name, build_race, build_commands = template
                # Check if the build order already exists in the database.
                existing_build = cls.get_build_by_name(build_name)
                if existing_build:
                    # Skip adding the build order if it already exists.
                    continue
                # Create a new PlayerBuildOrder instance for the new build order.
                new_build_template = BuildTemplate(
                    name=build_name, race=build_race, commands=build_commands
                )
                # Add the new build order template to the session.
                session.add(new_build_template)
            # Commit all the pending build order additions to the database.
            session.commit()

    @classmethod
    def get_unit_death_by_id(cls, unit_id: int) -> tuple[int, int, int]:
        """
        Retrieves a unit death by its ID. Returns the unit death details if found, otherwise logs a warning.

        :param unit_id: The ID of the unit death to retrieve.
        :return: A tuple with unit death details (id, time, resource) if found, otherwise None.
        """
        with cls.Session() as session:
            # Query for the unit death by ID and retrieve the first match (or None if not found).
            unit = session.query(UnitDeath).filter_by(id=unit_id).first()
            if unit:
                # Return the found unit death details as a tuple.
                return (unit.id, unit.time, unit.resource)
            else:
                # Log a warning if no unit death was found and return None.
                cls._log_name_not_found(unit_id)
                return None
            
    @classmethod
    def get_unit_deaths(cls) -> tuple:
        """
        Retrieves all unit deaths from the database and returns them as a tuple of tuples.

        :return: A tuple of tuples, each containing unit death details (id, time, resource).
        """
        with cls.Session() as session:
            # Use a generator expression to create a tuple of unit death details.
            units = tuple(
                (unit_death.id, unit_death.time, unit_death.resource)
                for unit_death in session.query(UnitDeath).all()
            )
            return units

    @classmethod
    def get_build_by_name(cls, build_name: str):
        """
        Retrieves a build order template by its name. Returns the build order details if found, otherwise logs a warning.
        """
        with cls.Session() as session:
            # Query for the build order by name and retrieve the first match (or None if not found).
            build = session.query(BuildTemplate).filter_by(name=build_name).first()
            if build:
                # Return the found build order details as a tuple.
                return (build.name, build.race, build.commands)
            else:
                # Log a warning if no build order template was found and return None.
                cls._log_name_not_found(build_name)
                return None

    @classmethod
    def get_builds(cls):
        """
        Returns all build order templates as a tuple of tuples.
        """
        with cls.Session() as session:
            # Use a generator expression to create a tuple of build order details.
            builds = tuple(
                (template.name, template.race, template.commands)
                for template in session.query(BuildTemplate).all()
            )
            return builds

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
                # Error handling
                cls._log_player_id_not_found(id, player)
                return None

    @classmethod
    def get_players_in_game(cls, game_id: int):
        with cls.Session() as session:
            plays = session.query(Play).filter_by(game_id=game_id).all()
            cls._check_game_id(game_id, plays)
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
            # Error handling
            cls.check_game_id_player_id(game_id, player_id, play)
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

    @classmethod
    def _log_name_not_found(cls, build_name):
        """
        Logs a warning message when a build order template name is not found in the database.
        """
        msg = f"Build: {build_name} - Build not found. - Ignore if adding build order to database"
        logging.warning(msg)

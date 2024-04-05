# Import any needed modules
from json import loads
import string
from sqlalchemy import create_engine
from sqlalchemy.orm import ClassManager, sessionmaker, strategies
# from database_tools.general.general_database import GeneralDB // Determine wheter you want to keep this file or not
from database_tools.sc2.entities.sc2_build_order_entities import PlayerBuildOrder


class SC2BuildOrderDB():
    """
    A class for interacting with the SC2 RTS build order database
    """
    engine = None
    Session = None

    @classmethod
    def init(cls, db_name):
        """
        Initializes database connection
        """
        # Establish connection to the database file
        cls.engine = create_engine(f"sqlite:///database_tools/data/{db_name}.db")
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls._build_order_id_count = 0

    @classmethod
    def add_build_orders(cls, build_order_list):
        with cls.Session() as session:
            for build_order in build_order_list:
                build_name = build_order[0]
                build_race = build_order[1]
                build_commands = build_order[2]
                existing_build_order = session.query(PlayerBuildOrder).filter_by(name=build_name).first()
                if existing_build_order:
                    continue
                build_order = PlayerBuildOrder(
                    ame=build_name,
                    race=build_race,
                    commands=build_commands,
                )
                session.add(build_order)
            session.commit()

    @classmethod
    def get_build_by_name(cls, build_name: string):
        with cls.Session() as session:
            build = session.query(PlayerBuildOrder).filter_by(name=build_name).first()
            if build:
                return (build.name, build.race, build.commands)
            else:
                return None

    @classmethod
    # FINISH LATER
    # def get_all_builds(cls):
    #     with cls.Session() as session:
    #         builds = tuple(
    #             (game.game_id, game.map, game.mode)
    #             for game in session.query(Game).all()
    #         )
    #         return games

    @classmethod
    def _create_build_order_id(cls) -> int:
        """Increment and return build order id"""
        cls._build_order_id_count += 1
        return cls._build_order_id_count 

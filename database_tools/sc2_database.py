# Import any needed modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_tools.entities.sc2_db_entities import (
    Base,
    Game,
    Play,
    Player,
    Issues,
    Command,
)


class SC2_DB:
    """A class for interacting with the SC2 database"""

    engine = None
    Session = None

    @classmethod
    def init(cls, db_name):
        cls.engine = create_engine(f"sqlite:///database_tools/{db_name}.db")
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    @classmethod
    def add_game(cls, mode, map, winner_id):
        with cls.Session() as session:
            game = Game(mode=mode, map=map, winner=winner_id)
            session.add(game)
            session.commit()

    @classmethod
    def add_player(cls, name, race):
        with cls.Session() as session:
            player = Player(name=name, race=race)
            session.add(player)
            session.commit()

    @classmethod
    def add_command(cls, name):
        with cls.Session() as session:
            command = Command(name=name)
            session.add(command)
            session.commit()

    @classmethod
    def get_player_info(cls, id):
        with cls.Session() as session:
            player = session.query(Player).filter_by(id=id).first()
            if player:
                return {
                    "player_id": player.id,
                    "name": player.name,
                    "race": player.race,
                }
            else:
                return None

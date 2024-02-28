
# Import any needed modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_tools.entities.sc2_db_entities import *


class SC2_DB:
    """A class for interacting with the SC2 database"""
    def __init__(self, db_name):
        self.engine = create_engine(f'sqlite:///database_tools/{db_name}.db')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.Session = Session

    def add_game(self, mode, map, winner_id):
        with self.Session() as session:
            game = Game(mode=mode, map=map, winner=winner_id)
            session.add(game)
            session.commit()

    def add_player(self, name, race):
        with self.Session() as session:
            player = Player(name=name, race=race)
            session.add(player)
            session.commit()

    def add_command(self, name):
        with self.Session() as session:
            command = Command(name=name)
            session.add(command)
            session.commit()

    def get_player_info(self, id):
        with self.Session() as session:
            player = session.query(Player).filter_by(player_id=id).first()
            if player:
                return {'player_id': player.player_id, 'name': player.name, 'race': player.race}
            else:
                return None

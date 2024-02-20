
# Import any needed modules
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# Base class for all tables
Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'
    game_id = Column(Integer, primary_key=True)
    mode = Column(String)
    map = Column(String)
    winner = Column(Integer, ForeignKey('players.player_id'))

class Player(Base):
    __tablename__ = 'players'
    player_id = Column(Integer, primary_key=True)
    name = Column(String)
    race = Column(String)
    # games = relationship('Game', backref='winner')

class Command(Base):
    __tablename__ = 'commands'
    command_id = Column(Integer, primary_key=True)
    name = Column(String)

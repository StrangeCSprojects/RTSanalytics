from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.schema import PrimaryKeyConstraint

Base = declarative_base()

class Game(Base):
    __tablename__ = "games"
    game_id = Column(Integer, primary_key=True)
    mode = Column(String)
    map = Column(String)

class Player(Base):
    __tablename__ = "players"
    player_id = Column(Integer, primary_key=True)
    name = Column(String)

class Play(Base):
    __tablename__ = "plays"
    game_id = Column(Integer, ForeignKey("games.game_id"), primary_key=True)
    player_id = Column(Integer, ForeignKey("players.player_id"), primary_key=True)
    race = Column(String)
    winner = Column(Boolean)
    commands = Column(String)

    # Define relationships
    game = relationship("Game", backref="plays")
    player = relationship("Player", backref="plays")

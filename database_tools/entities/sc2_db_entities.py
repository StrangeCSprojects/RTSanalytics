from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = "games"
    game_id = Column(Integer, primary_key=True)
    mode = Column(String)
    map = Column(String)
    winner_id = Column(Integer, ForeignKey("players.player_id"))  # Changed to 'winner_id'

    # Define relationship with the winning player
    winner = relationship("Player", foreign_keys=[winner_id])

class Player(Base):
    __tablename__ = "players"
    player_id = Column(Integer, primary_key=True)
    name = Column(String)
    race = Column(String)

class PlayerCommand(Base):
    __tablename__ = "commands"
    command_id = Column(Integer, primary_key=True)
    commands_list = Column(String)

class Issues(Base):
    __tablename__ = "issues"
    issue_id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("games.game_id"))
    player_id = Column(Integer, ForeignKey("players.player_id"))
    command_id = Column(Integer, ForeignKey("commands.command_id"))

    # Define relationships
    game = relationship("Game", backref="issues")
    player = relationship("Player", backref="issues")
    command = relationship("PlayerCommand")

class Play(Base):
    __tablename__ = "play"
    game_id = Column(Integer, ForeignKey("games.game_id"), primary_key=True)
    player_id = Column(Integer, ForeignKey("players.player_id"), primary_key=True)

    # Define relationships
    game = relationship("Game", backref="plays")
    player = relationship("Player", backref="plays")

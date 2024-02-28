
from sqlalchemy import Column, ForeignKey, Integer, String, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'
    game_id = Column(Integer, primary_key=True)
    mode = Column(String)
    map = Column(String)
    winner = Column(Integer, ForeignKey('players.player_id'))
    
    # Define relationship with players
    players = relationship("Player", backref="games")

class Player(Base):
    __tablename__ = 'players'
    player_id = Column(Integer, primary_key=True)
    name = Column(String)
    race = Column(String)

    # Define relationship with games
    games = relationship("Game", backref="players")

class Command(Base):
    __tablename__ = 'commands'
    command_id = Column(Integer, primary_key=True)
    name = Column(String)

class Issues(Base):
    __tablename__ = 'issues'
    game_id = Column(Integer, ForeignKey('games.game_id'), primary_key=True)
    player_id = Column(Integer, ForeignKey('players.player_id'), primary_key=True)
    command_id = Column(Integer, ForeignKey('commands.command_id'))
    
    # Define relationships
    game = relationship("Game")
    player = relationship("Player")
    command = relationship("Command")
    
    # Define composite primary key constraint
    __table_args__ = (
        PrimaryKeyConstraint('game_id', 'player_id'),
    )

class Play(Base):
    __tablename__ = 'play'
    game_id = Column(Integer, ForeignKey('games.game_id'), primary_key=True)
    player_id = Column(Integer, ForeignKey('players.player_id'), primary_key=True)
    
    # Define relationships
    game = relationship("Game", backref="plays")
    player = relationship("Player", backref="plays")

    # Define composite primary key constraint
    __table_args__ = (
        PrimaryKeyConstraint('game_id', 'player_id'),
    )

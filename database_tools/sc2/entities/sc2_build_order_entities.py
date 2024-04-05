from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.schema import PrimaryKeyConstraint

Base = declarative_base()

class PlayerBuildOrder(Base):
    __tablename__ = "build_order"
    name = Column(Integer, ForeignKey("games.game_id"), primary_key=True)
    player_id = Column(Integer, ForeignKey("players.player_id"), primary_key=True)
    race = Column(String)

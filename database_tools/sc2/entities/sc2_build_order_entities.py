from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.schema import PrimaryKeyConstraint

Base = declarative_base()

class PlayerBuildOrder(Base):
    __tablename__ = "build_order"
    name = Column(String, primary_key=True)
    race = Column(String)
    commands = Column(String) # Remember to use json.loads before storing commands

from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PlayerBuildOrder(Base):
    __tablename__ = "build_order"
    name = Column(String, primary_key=True)
    race = Column(String)
    commands = Column(String) # Remember to use json.loads before storing commands

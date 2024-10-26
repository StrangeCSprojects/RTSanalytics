from sqlalchemy import Column, String
from database_tools.sc2.entities.base import Base

class BuildTemplate(Base):
    __tablename__ = "build_template"
    name = Column(String, primary_key=True)
    race = Column(String)
    commands = Column(String) # Remember to use json.loads before storing commands

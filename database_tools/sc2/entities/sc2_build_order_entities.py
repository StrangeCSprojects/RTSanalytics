from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BuildTemplate(Base):
    __tablename__ = "build_template"
    name = Column(String, primary_key=True)
    race = Column(String)
    commands = Column(String) # Remember to use json.loads before storing commands

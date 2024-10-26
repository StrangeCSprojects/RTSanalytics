from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from database_tools.sc2.entities.base import Base

class UnitDeath(Base):
    """
    A SQLAlchemy model representing a record in the Major_Battles table.
    This table stores information about unit deaths in major battles.
    """

    __tablename__ = "unit_deaths"
    id = Column(Integer, primary_key=True)  # Integer column for the primary key 'id'
    time = Column(Integer)  # Integer column for the time of unit death
    resource = Column(
        Integer
    )  # Integer column for the resource value associated with the unit death

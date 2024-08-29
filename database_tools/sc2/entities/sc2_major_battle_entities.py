from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

# Creating a base class for declarative class definitions
Base = declarative_base()


class UnitDeath(Base):
    """
    A SQLAlchemy model representing a record in the Major_Battles table.
    This table stores information about unit deaths in major battles.
    """

    __tablename__ = "major_battles"  # Define the name of the table in the database

    # Define columns for the table
    id = Column(Integer, primary_key=True)  # Integer column for the primary key 'id'
    time = Column(Integer)  # Integer column for the time of unit death
    resource = Column(
        Integer
    )  # Integer column for the resource value associated with the unit death

from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

# Creating a base class for declarative class definitions
Base = declarative_base()


class UnitDeath(Base):
    """
    A SQLAlchemy model representing a record in the Major_Battles table.
    This table stores information about unit deaths in major battles.
    """

    __tablename__ = "Major_Battles"  # Define the name of the table in the database

    # Define columns for the table
    id = Column(int, primary_key=True)  # Integer column for the primary key 'id'
    time = Column(int)  # Integer column for the time of unit death
    resource = Column(
        int
    )  # Integer column for the resource value associated with the unit death

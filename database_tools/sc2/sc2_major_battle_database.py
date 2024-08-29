# Import necessary modules
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker,
)  # Import sessionmaker for database session management
from database_tools.general.general_database import (
    GeneralDB,
)  # Base class for general database interactions
from database_tools.sc2.entities.sc2_major_battle_entities import (
    UnitDeath,
    Base,
)  # ORM entities for SC2 major battles
import logging  # Import logging module for logging warnings and info


class SC2MajorBattleDB(GeneralDB):
    """
    A class for interacting with the SC2 RTS build order database.
    This class is designed to manage the database operations related to StarCraft II unit deaths,
    including initializing the database, adding new unit deaths, and retrieving existing unit deaths.
    """

    engine = None  # Class variable to hold the database engine once initialized.
    Session = None  # Class variable to hold the sessionmaker once the database is initialized.

    @classmethod
    def init(cls, db_name):
        """
        Initializes the database connection using the specified database name.
        This method sets up the SQLite engine and sessionmaker for interacting with the database.

        :param db_name: The name of the SQLite database file to connect to or create.
        """
        # Create an engine that stores data in the specified SQLite database file.
        cls.engine = create_engine(f"sqlite:///database_tools/data/{db_name}.db")
        # Create all tables in the database (if not already existing) based on ORM entities.
        Base.metadata.create_all(cls.engine)
        # Create a configured "Session" class bound to the database engine.
        cls.Session = sessionmaker(bind=cls.engine)
        # Initialize a counter for unit death IDs (optional, could be used internally if needed)
        cls._unit_death_id_count = 0

    @classmethod
    def add_unit_deaths(cls, unit_death_list: list[tuple[int, int, int]]) -> None:
        """
        Adds multiple unit deaths to the database from a list of unit deaths.

        :param unit_death_list: A list of tuples, where each tuple contains unit death details (id, time, resource).
        """
        with cls.Session() as session:
            for unit_death in unit_death_list:
                # Unpack the unit death tuple into its components.
                id, time, resource = unit_death

                # Create a new UnitDeath instance for the new unit death.
                unit_death = UnitDeath(id=id, time=time, resource=resource)
                # Add the new unit death to the session.
                session.add(unit_death)
            # Commit all the pending unit death additions to the database.
            session.commit()

    @classmethod
    def get_unit_death_by_id(cls, unit_id: int) -> tuple[int, int, int]:
        """
        Retrieves a unit death by its ID. Returns the unit death details if found, otherwise logs a warning.

        :param unit_id: The ID of the unit death to retrieve.
        :return: A tuple with unit death details (id, time, resource) if found, otherwise None.
        """
        with cls.Session() as session:
            # Query for the unit death by ID and retrieve the first match (or None if not found).
            unit = session.query(UnitDeath).filter_by(id=unit_id).first()
            if unit:
                # Return the found unit death details as a tuple.
                return (unit.id, unit.time, unit.resource)
            else:
                # Log a warning if no unit death was found and return None.
                cls._log_name_not_found(unit_id)
                return None

    @classmethod
    def get_unit_deaths(cls) -> tuple:
        """
        Retrieves all unit deaths from the database and returns them as a tuple of tuples.

        :return: A tuple of tuples, each containing unit death details (id, time, resource).
        """
        with cls.Session() as session:
            # Use a generator expression to create a tuple of unit death details.
            units = tuple(
                (unit_death.id, unit_death.time, unit_death.resource)
                for unit_death in session.query(UnitDeath).all()
            )
            return units

    @classmethod
    def _log_name_not_found(cls, unit_id: int) -> None:
        """
        Logs a warning message when a unit death ID is not found in the database.

        :param unit_id: The ID of the unit death that was not found.
        """
        msg = f"Unit: {unit_id} - Unit not found. - Ignore if adding unit to database"
        logging.warning(msg)

# Import any needed modules
from sqlalchemy import create_engine
from sqlalchemy.orm import ClassManager, sessionmaker, strategies
from database_tools.general.general_database import GeneralDB
from database_tools.sc2.entities.sc2_build_order_entities import BuildTemplate, Base
import os
import configparser
import psycopg2
import logging


class SC2RTSADB(GeneralDB):
    """
    A singleton class acting as an interface to the RTS Analytics database for StarCraft II.
    This class is designed to manage the database operations related to StarCraft II
    build orders, game replays, and major battles.
    """

    engine = None  # Static variable to hold the database engine once initialized.
    Session = None  # Static variable to hold the sessionmaker once the database is initialized.

    @classmethod
    def init(cls):
        """
        This method sets up the PostgreSQL engine and sessionmaker for interacting with the database.

        NOTE: You must have a "config.ini" file in the current directory.
            (see README.md for more information)
        """
        
        # First get the path to the config file dynamically
        current_directory = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_directory, 'config.ini')

        # Load the config file
        config = configparser.ConfigParser()
        config.read(config_path)

        # Retrieve credentials from the config file
        username = config['database']['username']
        password = config['database']['password']
        host = config['database']['host']
        port = config['database']['port']
        database = config['database']['database']

        # Create an engine that stores data in the specified PostgreSQL database
        cls.engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")
        
        # Create a configured "Session" class bound to the database engine
        cls.Session = sessionmaker(bind=cls.engine)

        # Create all tables in the database (if not already existing) based on metadata.
        Base.metadata.create_all(cls.engine)

        # Initialize a counter for build order IDs
        cls._build_order_id_count = 0 # TODO: MAY NOT NEED TO DO THIS NOW THAT WE HAVE POSTGRES


    @classmethod
    def add_build_templates(cls, build_templates):
        """
        Adds multiple build templates to the database from a list of build orders.
        Each template in the list is checked for existence before addition to prevent duplicates.
        """
        with cls.Session() as session:
            for template in build_templates:
                # Decompose the tuple into its components.
                build_name, build_race, build_commands = template
                # Check if the build order already exists in the database.
                existing_build = cls.get_build_by_name(build_name)
                if existing_build:
                    # Skip adding the build order if it already exists.
                    continue
                # Create a new PlayerBuildOrder instance for the new build order.
                new_build_template = BuildTemplate(
                    name=build_name, race=build_race, commands=build_commands
                )
                # Add the new build order template to the session.
                session.add(new_build_template)
            # Commit all the pending build order additions to the database.
            session.commit()

    @classmethod
    def get_build_by_name(cls, build_name: str):
        """
        Retrieves a build order template by its name. Returns the build order details if found, otherwise logs a warning.
        """
        with cls.Session() as session:
            # Query for the build order by name and retrieve the first match (or None if not found).
            build = session.query(BuildTemplate).filter_by(name=build_name).first()
            if build:
                # Return the found build order details as a tuple.
                return (build.name, build.race, build.commands)
            else:
                # Log a warning if no build order template was found and return None.
                cls._log_name_not_found(build_name)
                return None

    @classmethod
    def get_builds(cls):
        """
        Returns all build order templates as a tuple of tuples.
        """
        with cls.Session() as session:
            # Use a generator expression to create a tuple of build order details.
            builds = tuple(
                (template.name, template.race, template.commands)
                for template in session.query(BuildTemplate).all()
            )
            return builds

    @classmethod
    def _log_name_not_found(cls, build_name):
        """
        Logs a warning message when a build order template name is not found in the database.
        """
        msg = f"Build: {build_name} - Build not found. - Ignore if adding build order to database"
        logging.warning(msg)


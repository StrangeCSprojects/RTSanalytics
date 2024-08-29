from json import loads  # Import the loads function for JSON deserialization.
import string  # Import the string module for potential string manipulation.
from database_tools.general.data_retriever import (
    DataRetriever,
)  # Base class for data retrieval operations.
from database_tools.sc2.sc2_major_battle_database import (
    SC2MajorBattleDB,
)  # Import SC2 database class for major battle data.
import logging  # Import logging module for logging warnings and information.


class SC2MajorBattleDataRetriever(DataRetriever):
    """
    A subclass of DataRetriever tailored for retrieving StarCraft II unit death data.
    This class extends the functionality of DataRetriever to suit the specific needs
    of accessing and analyzing StarCraft II unit death data.
    """

    def __init__(self, database: SC2MajorBattleDB) -> None:
        """
        Initialize the SC2BuildOrderDataRetriever with a database connection or configuration.

        :param database: An instance of SC2MajorBattleDB used for data retrieval.
        """
        super().__init__(
            database
        )  # Calls the initializer of the superclass (DataRetriever).

    def get_all_unit_deaths(self) -> tuple:
        """
        Retrieves all unit deaths from the database.

        :return: A tuple of unit deaths from the database.
        """
        # Remember to call the loads function on the command list if JSON deserialization is needed.

        death_list = (
            self.database.get_unit_deaths()
        )  # Get all unit deaths from the database.

        # Error handling to log a warning if the retrieved list is empty.
        self._log_build_list_database_empty(death_list)
        return death_list

    def _log_build_list_database_empty(self, death_list: tuple) -> None:
        """
        Logs a warning message if the retrieved unit death list from the database is empty.

        :param death_list: A tuple of unit deaths retrieved from the database.
        """
        if (
            len(death_list) == 0
        ):  # Checks if the unit death list from the database is empty.
            msg = "No unit deaths in database"  # Warning message to be logged.
            logging.warning(msg)

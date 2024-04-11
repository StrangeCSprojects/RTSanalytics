from json import loads
import string
from database_tools.general.data_retriever import DataRetriever
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB


class SC2BuildOrderDataRetriever(DataRetriever):
    """
    A subclass of DataRetriever tailored for retrieving StarCraft II build order data.
    This class leverages inheritance to extend or modify the functionality of the DataRetriever
    class to suit the specific needs of accessing and analyzing StarCraft II build order data.
    """

    def __init__(self, database: SC2BuildOrderDB) -> None:
        """
        Initialize the SC2BuildOrderDataRetriever with a database connection or configuration.

        :param database: The database connection or configuration to be used for data retrieval.
        """
        super().__init__(
            database
        )  # Calls the initializer of the superclass (DataRetriever)

    # def get_build_by_name(self, build_name: str):
    #     """
    #     Retrieve a single build order by specifying its name
    #     """
    #     return self.database.get_build_by_name(build_name)
    
    def get_build_by_name(self, build_name: str):
        """
        Retrieve a single build order by specifying its name
        """
        build = self.database.get_build_by_name(build_name)
        if not build:
            return None
        race = build[1]

        serialized_commands = build[2]
        temp_commands = loads(serialized_commands)

        # turning list of lists, into a list of tuples
        result_commands = [((tuple(inner_list[0][0]), inner_list[0][1]), inner_list[1]) for inner_list in temp_commands]

        result = (race, result_commands)

        return result

    def get_all_builds_by_race(self, race: str):
        """
        Retrieve all build orders with a specified race
        """
        result = []
        all_builds = self.database.get_builds()
        for build in all_builds:
            if build[1] != race:
                continue
            serialized_commands = build[2]
            temp_result = loads(serialized_commands)

            # turning list of lists, into a list of tuples
            result_commands = [((tuple(inner_list[0][0]), inner_list[0][1]), inner_list[1]) for inner_list in temp_result]
            result.append((build[0], result_commands))

        return result

    def get_all_builds(self):
        """
        Returns all the builds in the build order database
        """
        # REMEMBER TO CALL THE LOADS FUNCTION ON THE COMMAND LIST
        return self.database.get_builds()

    # def get_commands(self, build_order_name: str):
    #     """
    #     Retrieve data about a single command from the database.
    #     """
    #     play = self.get_play(game_id, player_id)
    #     serialized_commands = play[2]
    #     temp_result = loads(serialized_commands)

    #     # turning list of lists, into a list of tuples
    #     result = [(tuple(inner_list[0]), inner_list[1]) for inner_list in temp_result]

    #     return result

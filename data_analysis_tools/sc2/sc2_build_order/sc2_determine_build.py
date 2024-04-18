from data_analysis_tools.general.determine_build import DetermineBuild
from database_tools.sc2.sc2_build_order_data_retriever import SC2BuildOrderDataRetriever
import logging
from config.sc2_logging_config import setup_logging

# Setup logging capabilites
setup_logging()
compare_builds_logger = logging.getLogger("comparing_builds")


class SC2DetermineBuild(DetermineBuild):
    """
    Extends DetermineBuild to implement a method for determining the build strategy for a
    StarCraft II race based on gameplay commands. Supports Zerg, Protoss, and Terran races.
    """

    def __init__(self, data_retriever: SC2BuildOrderDataRetriever) -> None:
        """
        Initializes the SC2DetermineBuild object, compares user builds against the benchmark
        builds from the sc2_build_order_database (via sc2_data_retriever) to determine
        which benchmark build the user build is most similar to.

        Parameters:
            data_retriever: retrieves build order data from the sc2_build_order_database
        """
        super().__init__(data_retriever)

    def determine_build(
        self, race: str, user_commands: list[tuple[tuple[str, str], int]]
    ) -> str:
        """
        Compares the user's build against all builds of the same race in the sc2_build_order_database
        and returns the build that has the highest accuracy of at least 50%. If the user's build doesn't
        match any build at least 50% then just returns misc.

        Parameters:
            race: The race for which to determine the build (Zerg, Protoss, or Terran).
            user_commands: A list of tuples, each containing a tuple (command type, command name) and the time executed.

        Returns:
            str: The determined build strategy or misc if none can be determined.
        """
        # Error handling
        self._log_user_commands(user_commands)

        confidence_scores = (
            {}
        )  # dictionary containing each build order and the percent of similarity to the user's build

        # user build should at least reach 50% or defaults to misc. build
        highest_accuracy = 10
        closest_build_order = "Misc."

        # iterate through each build of the same race in the database
        for benchmark_build in self.data_retriever.get_all_builds_by_race(race):
            benchmark_name = benchmark_build[0]  # name of build
            benchmark_commands = benchmark_build[
                1
            ]  # tuple(tuple(tuple(unit_type, unit_name),time),weight)
            confidence_scores[benchmark_name] = self._compare_build_orders(
                benchmark_commands, user_commands
            )

            # Error handling
            self._log_confidence_scores(
                benchmark_build, confidence_scores[benchmark_name]
            )

        # find the build that is most similar to the user's build
        for score in confidence_scores:
            if confidence_scores[score] >= highest_accuracy:
                highest_accuracy = confidence_scores[score]
                closest_build_order = score

        # Error handling
        self._check_build_found(closest_build_order)
        self._log_build_match(closest_build_order)

        return closest_build_order

    def _compare_build_orders(
        self,
        benchmark_commands: list[tuple[tuple[tuple[str, str], int]], float],
        user_commands: list[tuple[tuple[str, str], int]],
    ) -> float:
        """
        Helper method, compares the user's build to one of the benchmark builds and returns the relative error
        between them.

        Parameters:
            benchmark_commands: The list of commands from the benchmark build. Contains: Unit, Name, Time, Weight
            user_commands: The list of commands from the user build. Contains: Unit, Name, Time

        Returns:
            Percent number of how similar the two builds are
        """
        # used to sort the units by types
        benchmark_unit_dictionary = {}
        user_unit_dictionary = {}
        relative_error_list = []

        # sort the units by types
        for command in benchmark_commands:
            benchmark_unit = command[0][0]  # (unit_type, unit_name)
            benchmark_time = command[0][1]  # time the unit was recorded
            benchmark_weight = command[
                1
            ]  # value used in weighted average, determines how important unit is to build
            self._load_unit_dictionary(
                benchmark_unit_dictionary, benchmark_unit, benchmark_time
            )

        # sort the units by types
        for command in user_commands:
            command_unit = command[0]  # (unit_type, unit_name)
            command_time = command[1]  # time the unit was recorded
            self._load_unit_dictionary(user_unit_dictionary, command_unit, command_time)

        for unit_type in benchmark_unit_dictionary:
            # matches up the user unit types with the benchmark unit types
            try:
                user_unit_dictionary[unit_type]
            except KeyError:
                user_unit_dictionary[unit_type] = []

            # pad user unit types to match benchmark user types if necessary
            if len(user_unit_dictionary[unit_type]) < len(
                benchmark_unit_dictionary[unit_type]
            ):
                self._pad_user_unit_dictionary(
                    benchmark_unit_dictionary, user_unit_dictionary, unit_type
                )

            relative_error_list.append(
                self._relative_error_of_unit_type(
                    benchmark_unit_dictionary, user_unit_dictionary, unit_type
                )
            )

            # Error handling
            self._log_RE_unit_types(
                unit_type, benchmark_unit_dictionary, user_unit_dictionary
            )

        # Error handling
        self._log_benchmark_dictionary(benchmark_unit_dictionary)
        self._log_user_dictionary(user_unit_dictionary)

        mean_relative_error = sum(relative_error_list) / len(relative_error_list)

        percent_similarity = (1 - mean_relative_error) * 100

        return percent_similarity

    def _relative_error_of_unit_type(
        self,
        benchmark_unit_dictionary: dict[tuple[str, str] : list[int]],
        user_unit_dictionary: dict[tuple[str, str] : list[int]],
        unit_type: tuple[str, str],
    ) -> float:
        """
        Helper method, compares the user's build to one of the benchmark builds and returns the relative error
        between them.

        Parameters:
            benchmark_unit_dictionary: Dict{unit_type:{list of times}}, a dictionary of all the times unit_types are created
            user_unit_dictionary: Dict{unit_type:{list of times}}, a dictionary of all the times unit_types are created
            unit_type: The type of unit I.E. (InitUnitEvent, SCV)

        Returns:
            Percent number of how similar the two builds are
        """

        relative_error_list = []  # contains all the relative errors

        # gets the error between the benchmark unit and user unit with the corresponding unit type
        for benchmark_unit, user_unit in zip(
            benchmark_unit_dictionary[unit_type],
            user_unit_dictionary[unit_type],
        ):
            benchmark_unit = int(benchmark_unit)
            absolute_error = abs(benchmark_unit - user_unit)
            relative_error = absolute_error / benchmark_unit

            # relative error can't be greater than one
            if relative_error > 1:
                relative_error = 1
            relative_error_list.append(relative_error)
        mean_relative_error = sum(relative_error_list) / len(relative_error_list)
        return mean_relative_error

    def _load_unit_dictionary(
        self,
        unit_dictionary: dict[tuple[str, str] : list[int]],
        unit_type: tuple[str, str],
        time: int,
    ) -> None:
        """
        Helper method, loads the unit and its corresponding time into a dictionary.

        Parameters:
            unit_dictionary: Dict{unit_type:{list of times}}, a dictionary of all the times unit_types are created
            unit_type: The type of unit I.E. (InitUnitEvent, SCV)
            time: Time unit was created
        """
        if unit_type not in unit_dictionary:
            unit_dictionary[unit_type] = []
        unit_dictionary[unit_type].append(time)

    def _pad_user_unit_dictionary(
        self,
        benchmark_unit_dictionary: dict[tuple[str, str] : list[int]],
        user_unit_dictionary: dict[tuple[str, str] : list[int]],
        unit_type: tuple[str, str],
    ) -> None:
        """
        Helper method, pads the user_unit_dictionary[unit_type] with times of 10,000 so that the
        user_unit_dictionary is the same size as the benchmark_unit_dictionary

        Parameters:
            benchmark_unit_dictionary: Dict{unit_type:{list of times}}, a dictionary of all the times unit_types are created
            user_unit_dictionary: Dict{unit_type:{list of times}}, a dictionary of all the times unit_types are created
            unit_type: The type of unit I.E. (InitUnitEvent, SCV)
        """
        while len(user_unit_dictionary[unit_type]) < len(
            benchmark_unit_dictionary[unit_type]
        ):
            user_unit_dictionary[unit_type].append(10000)

    # Error handling methods
    def _log_confidence_scores(self, build, c_score):
        # Logs the confidence score associated with a specific build.
        compare_builds_logger.info(f"Build: {build[0]} - Confidence Score: {c_score}")

    def _log_RE_unit_types(
        self, unit_type, benchmark_unit_dictionary, user_unit_dictionary
    ):
        # Calculates the relative error between benchmark and user unit types for a given unit type.
        re = self._relative_error_of_unit_type(
            benchmark_unit_dictionary, user_unit_dictionary, unit_type
        )
        # Logs the relative error along with the benchmark and user values for that unit type.
        msg = f"Unit Type: {unit_type} - Relative Error: {re} - Benchmark: {benchmark_unit_dictionary[unit_type]} - User: {user_unit_dictionary[unit_type]}"
        compare_builds_logger.info(msg)

    def _check_build_found(self, build_order):
        # Checks if the provided build order is labeled as "Misc.", indicating no matching build was found.
        if build_order == "Misc.":
            # Raises a ValueError if no matching build is found.
            raise ValueError("No matching build found")

    def _log_user_commands(self, commands):
        # Logs the list of commands provided by the user.
        msg = f"User Commands: {commands}"
        compare_builds_logger.info(msg)

    def _log_benchmark_dictionary(self, benchmark_unit_dictionary):
        # Logs the entire benchmark unit dictionary to trace or debug information.
        msg = f"Bechmark Unit Dictionary: {benchmark_unit_dictionary}"
        compare_builds_logger.info(msg)

    def _log_user_dictionary(self, user_unit_dictionary):
        # Logs the entire user unit dictionary to trace or debug information.
        msg = f"User Unit Dictionary: {user_unit_dictionary}"
        compare_builds_logger.info(msg)

    def _log_build_match(self, match):
        # Logs a message indicating a successful build match.
        msg = f"Matching Build: {match}"
        compare_builds_logger.info(msg)

from data_analysis_tools.general.build_order.build_order_creator import (
    BuildOrderCreator,
)

from database_tools.sc2.sc2_build_order_access import BuildOrderDataStorage
import csv
import logging
from config.sc2_logging_config import setup_logging
import os

setup_logging()


class SC2BuildOrderCreator(BuildOrderCreator):
    """
    creates StarCraft II (SC2) build orders from CSV files. This class reads a
    specified CSV file, processes the contained commands, and stores them using
    a data accesser.
    """

    def __init__(self) -> None:
        """
        Initializes the SC2BuildOrderCreator object and sets
        up a BuildOrderStorage instance to hold the
        build data that will be read from the CSV file.
        """
        super().__init__()
        # Initialize the build data storage.
        self._build_data = BuildOrderDataStorage()

    def create_build(self, name: str, race: str, file_name: str) -> None:
        """
        Reads a CSV file containing SC2 build commands, processes each command,
        and stores them into the build data storage. Each command in the CSV is
        expected to have at least four columns: two identifying the unit, one for
        the time the command is to be executed, and one for the command's weight.

        Parameters:
            file_name: The name of the CSV file within the sc2_build directory
                       containing the build commands.
        """
        # Check file is .csv
        self._check_file_type(file_name)

        # Form the full path to the CSV file within the sc2_build directory.
        directory_path = "data_analysis_tools/sc2/sc2_build_order/build_orders/"
        file_path = os.path.join(directory_path, file_name)

        # Check file opens properly
        self._check_file_opens(file_path)

        # Open and read the CSV file.
        with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            # Check for correct headers
            headers = next(csv_reader, None)
            self._check_headers(headers)

            # Initialize a list to hold the commands parsed from the CSV file.
            commands_list = []

            # Used in error handling
            previous_time = 0
            previous_command = ""

            # Loop through the remaining rows in the CSV file.
            for command in csv_reader:

                # Check that length of every command is 4
                self._check_command_length(name, command)

                # Extract the unit, time, and weight for each command.
                unit = (command[0], command[1])
                time = command[2]
                weight = command[3]

                # Check that time of earlier commands is less than that of later commands
                self._check_command_time(
                    previous_command, previous_time, command, time, name
                )

                # Check that weights are between 0-1
                self._check_command_weight(name, command, weight)

                # Package the command details and add to the commands list.
                command_package = ((unit, time), weight)
                commands_list.append(command_package)

                # Used in error handling
                previous_command = command
                previous_time = time

            # Store the processed commands in the build data storage and
            # then push the data to the underlying system or database.
            build_order = (name, race, commands_list)
            self._build_data.set_data(build_order)
            self._build_data.push()

    # Error handling methods
    def _check_file_type(self, file_name):
        # Checks if the file name ends with ".csv" extension.
        if not file_name.endswith(".csv"):
            # Constructs a custom error message.
            msg = f"'{file_name}' needs to be converted to a csv file"
            # Logs an error message indicating the file does not have a CSV extension.
            logging.error(msg)
            # Raises a ValueError exception with the custom message.
            raise ValueError(msg)

    def _check_file_opens(self, file_path):
        # Attempts to open the specified file in read mode.
        try:
            file = open(file_path, "r")
            # Closes the file immediately after opening, if successful.
            file.close()
        except FileNotFoundError as error:
            # Logs an error if the file is not found.
            msg = f"{error}"
            logging.error(msg)

    def _check_command_length(self, build, command):
        # Checks if the length of the command is exactly 4.
        if len(command) != 4:
            # Constructs and logs a debug message if the command length is incorrect.
            msg = f"Build Order: {build} - Command: {command} - Incorrect Length: {len(command)}"
            logging.debug(msg)
            # Raises a ValueError if the command length is not 4.
            raise ValueError(msg)

    def _check_headers(self, headers):
        # Defines a list of required headers.
        required_headers = [
            "Unit_Type",
            "Unit_Name",
            "Time (seconds)",
            "Weight (default =1)",
        ]
        # Checks if provided headers match the required headers.
        if headers != required_headers:
            # Constructs and logs a debug message if headers do not match.
            msg = (
                f"Headers: {headers} do not match Required Headers: {required_headers}"
            )
            logging.debug(msg)
            # Raises a ValueError if headers do not match the required list.
            raise ValueError(msg)

    def _check_command_time(
        self, previous_command, previous_time, current_command, current_time, build_name
    ):
        # Checks if the previous command time is greater than the current command time.
        if int(previous_time) > int(current_time):
            # Constructs and logs a debug message for the command time error.
            msg = f"Previous Command was given after Current Command - Previous Command: {previous_command} - Previous Time: {previous_time} - Current Command: {current_command} - Current Time: {current_time} - Build: {build_name}"
            logging.debug(msg)
            # Raises a ValueError if the previous command time is after the current command time.
            raise ValueError(msg)

    def _check_command_weight(self, name, command, weight):
        # Checks if the command weight is between 0 and 1, inclusive.
        if (int(weight) < 0) or (int(weight) > 1):
            # Constructs and logs a debug message if the weight is out of the acceptable range.
            msg = f"Build: {name} - Command: {command} - Weight: {weight} - Weight must be between 0-1"
            logging.debug(msg)
            # Raises a ValueError if the weight is not within the required range.
            raise ValueError(msg)

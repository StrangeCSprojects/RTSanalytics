from data_analysis_tools.general.build_order.build_order_creator import (
    BuildOrderCreator,
)

from database_tools.sc2.sc2_build_order_access import BuildOrderDataStorage

import csv

import logging
from config.sc2_logging_config import setup_logging
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

    def create_build(self, name:str, race:str, file_name: str) -> None:
        """
        Reads a CSV file containing SC2 build commands, processes each command,
        and stores them into the build data storage. Each command in the CSV is
        expected to have at least four columns: two identifying the unit, one for
        the time the command is to be executed, and one for the command's weight.

        Parameters:
            file_name: The name of the CSV file within the sc2_build directory
                       containing the build commands.
        """
        self._check_file_type(file_name)

        # Form the full path to the CSV file within the sc2_build directory.
        file_path = f"sc2_build/{file_name}"

        self._check_file_opens(file_path)

        # Open and read the CSV file.
        with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            # Skip the first line of the CSV file, which typically contains headers.
            headers = next(csv_reader, None)

            self._check_headers(headers)

            # Initialize a list to hold the commands parsed from the CSV file.
            commands_list = []

            previous_time = 0
            previous_command = ""

            # Loop through the remaining rows in the CSV file.
            for command in csv_reader:
                
                self._check_command_length(name, command)

                # Extract the unit, time, and weight for each command.
                unit = (command[0], command[1])
                time = command[2]
                weight = command[3]

                self._check_command_time(previous_command, previous_time, command, time, name)
                self._check_command_weight(name, command, weight)

                # Package the command details and add to the commands list.
                command_package = ((unit, time), weight)
                commands_list.append(command_package)

                previous_command = command
                previous_time = time


            # Store the processed commands in the build data storage and
            # then push the data to the underlying system or database.
            build_order = (name, race, commands_list)
            self._build_data.set(build_order)
            self._build_data.push()

    def _check_file_type(self, file_name):
        if not file_name.endswith(".csv"):
            msg = f"'{file_name}' needs to be converted to a csv file"
            logging.error(msg)
            raise ValueError(msg)

    def _check_file_opens(self, file_path):
        try:
            file = open(file_path, 'r')
            file.close()
        except FileNotFoundError as error:
            msg = f"{error}"
            logging.error(msg)

    def _check_command_length(self, build, command):
        if len(command) != 4:
            msg = f"Build Order: {build} - Command: {command} - Incorrect Length: {len(command)}"
            logging.debug(msg)
            raise ValueError(msg)
    
    def _check_headers(self, headers):
        required_headers = ['Unit_Type', 'Unit_Name', 'Time (seconds)', 'Weight (default = 1)']
        if headers != required_headers:
            msg = f"Headers: {headers} do not match Required Headers: {required_headers}"
            logging.debug(msg)
            raise ValueError(msg)

    def _check_command_time(previous_command, previous_time, current_command, current_time, build_name):
        if previous_time > current_time:
            msg = f"Previous Command was given after Current Command - Previous Command: {previous_command} - Previous Time: {previous_time} - Current Command: {current_command} - Current Time: {current_time} - Build: {build_name}"
            logging.debug(msg)
            raise ValueError(msg)

    def _check_command_weight(name, command, weight):
        if (weight < 0) or (weight > 1):
            msg = f"Build: {name} - Command: {command} - Weight: {weight} - Weight must be between 0-1"
            logging.debug(msg)
            raise ValueError(msg)

test = SC2BuildOrderCreator()
test.create_build("test", "test", "testme.docx")
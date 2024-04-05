from data_analysis_tools.general.build_order.build_order_creator import (
    BuildOrderCreator,
)
import csv


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
        self._build_data = BuildOrderStorage()

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
        # Form the full path to the CSV file within the sc2_build directory.
        file_path = f"sc2_build/{file_name}"

        # Open and read the CSV file.
        with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            # Skip the first line of the CSV file, which typically contains headers.
            next(csv_reader, None)

            # Initialize a list to hold the commands parsed from the CSV file.
            commands_list = []

            # Loop through the remaining rows in the CSV file.
            for command in csv_reader:
                # Extract the unit, time, and weight for each command.
                unit = (command[0], command[1])
                time = command[2]
                weight = command[3]

                # Package the command details and add to the commands list.
                command_package = ((unit, time), weight)
                commands_list.append(command_package)

            # Store the processed commands in the build data storage and
            # then push the data to the underlying system or database.
            build_order = (name, race, commands_list)
            self._build_data.set(build_order)
            self._build_data.push()

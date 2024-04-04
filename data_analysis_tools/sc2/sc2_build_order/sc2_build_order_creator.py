from data_analysis_tools.general.build_order.build_order_creator import BuildOrderCreator
import csv
class SC2BuildOrderCreator(BuildOrderCreator):
    def __init__(self) -> None:
        super().__init__()
        self._build_data = BuildOrderStorage()

    def create_build(self, file_name: str) -> None:
        file_path = f"sc2_build/{file_name}"

        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader, None)

            commands_list = []

            for command in csv_reader:
                unit = (command[0], command[1])
                time = command[2]
                weight = command[3]

                command_package = ((unit, time), weight)
                commands_list.append(command_package)

        self._build_data.set(commands_list)
        self._build_data.push()






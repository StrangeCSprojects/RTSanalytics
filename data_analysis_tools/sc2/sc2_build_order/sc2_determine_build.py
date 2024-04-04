from data_analysis_tools.general.determine_build import DetermineBuild
from data_analysis_tools.sc2.sc2_data_retriever import SC2DataRetriever


class SC2DetermineBuild(DetermineBuild):
    """
    Extends DetermineBuild to implement a method for determining the build strategy for a
    StarCraft II race based on gameplay commands. Supports Zerg, Protoss, and Terran races.
    """

    def __init__(self, sc2_data_retriever:SC2DataRetriever) -> None:
        """
        Initializes the SC2DetermineBuild object with build management instances for each race.
        Sets up a tuple containing all race build instances for later use.
        """
        super().__init__(sc2_data_retriever)

    def determine_build(self, race: str, user_commands: list[tuple[tuple[str,str],int]]) -> str:
        """


        Parameters:
            race (str): The race for which to determine the build (Zerg, Protoss, or Terran).
            commands (list[tuple[tuple[command_type, command_name],time]])): A list of tuples, each containing a tuple (command type, command name) and the time executed.

        Returns:
            str: The determined build strategy or an error message if the race is not recognized.
        """
        confidence_scores = {}

        for benchmark_build in self.data_retriever.get_all_builds_of_race(race):

            benchmark_name = benchmark_build[0] # name of build
            benchmark_commands = benchmark_build[1] # tuple(tuple(tuple(unit_type, unit_name),time),weight)
           

            confidence_scores[benchmark_name] = self._compare_build_orders(benchmark_commands, user_commands)

    def _compare_build_orders(self, benchmark_commands:list[tuple[tuple[tuple[str,str],int]], float], user_commands) -> float:
        """


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
            benchmark_unit = command[0][0] # (unit_type, unit_name)
            benchmark_time = command[0][1] # time the unit was recorded
            benchmark_weight = command[1] # value used in weighted average, determines how important unit is to build
            
            self._load_unit_dictionary(benchmark_unit_dictionary, benchmark_unit, benchmark_time)
        

        # sort the units by types
        for command in user_commands:
            command_unit = command[0][0] # (unit_type, unit_name)
            command_time = command[0][1] # time the unit was recorded
        
            self._load_unit_dictionary(user_unit_dictionary, command_unit, command_time)
    


        for unit_type in benchmark_unit_dictionary:

            # matches up the user unit types with the benchmark unit types
            try:
                user_unit_dictionary[unit_type]
            except KeyError:
                user_unit_dictionary[unit_type] = []

            # pad user unit types to match benchmark user types if necessary
            if len(user_unit_dictionary[unit_type]) < len(benchmark_unit_dictionary[unit_type]):
                self._pad_user_unit_dictionary(benchmark_unit_dictionary, user_unit_dictionary, unit_type)

            relative_error_list.append(self._relative_error_of_unit_type(benchmark_unit_dictionary, user_unit_dictionary, unit_type))

            mean_relative_error = sum(relative_error_list) / len(relative_error_list)

            return mean_relative_error        
        
    def _relative_error_of_unit_type(self, benchmark_unit_dictionary, user_unit_dictionary, unit_type):

        relative_error_list = []

        for benchmark_unit, user_unit in (benchmark_unit_dictionary[unit_type], user_unit_dictionary[unit_type]):
            absolute_error = abs(benchmark_unit - user_unit)
            relative_error = absolute_error / benchmark_unit

            # relative error can't be greater than one
            if relative_error > 1:
                relative_error = 1

            relative_error_list.append(relative_error)

        mean_relative_error = sum(relative_error_list) / len(relative_error_list)

        return mean_relative_error

    def _load_unit_dictionary(self, unit_dictionary, unit, time):

        if unit not in unit_dictionary:
            unit_dictionary[unit] = []
        unit_dictionary[unit].append(time)

    def _pad_user_unit_dictionary(self, benchmark_unit_dictionary, user_unit_dictionary, unit_type):
        while len(user_unit_dictionary[unit_type]) < len(benchmark_unit_dictionary[unit_type]):
            user_unit_dictionary[unit_type] = 10000

                


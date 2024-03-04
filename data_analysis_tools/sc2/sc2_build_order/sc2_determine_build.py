from data_analysis_tools.general.determine_build import DetermineBuild
from data_analysis_tools.sc2.sc2_build_order.sc2_race_builds import (
    ZergBuilds,
    ProtossBuilds,
    TerranBuilds,
)


class SC2DetermineBuild(DetermineBuild):
    """
    Extends DetermineBuild to implement a method for determining the build strategy for a
    StarCraft II race based on gameplay commands. Supports Zerg, Protoss, and Terran races.
    """

    def __init__(self) -> None:
        """
        Initializes the SC2DetermineBuild object with build management instances for each race.
        Sets up a tuple containing all race build instances for later use.
        """
        super().__init__()
        self.zerg_builds = ZergBuilds()
        self.protoss_builds = ProtossBuilds()
        self.terran_builds = TerranBuilds()
        self.race_types = (self.zerg_builds, self.protoss_builds, self.terran_builds)

    def determine_build(self, race: str, commands: list[tuple]) -> str:
        """
        Determines the build based on the race and a list of commands executed in the game.
        Filters commands relevant to the economy and non-economy aspects up to 5 minutes and 30 seconds,
        then calculates resources allocated to each aspect to decide on the build strategy.

        Parameters:
            race (str): The race for which to determine the build (Zerg, Protoss, or Terran).
            commands (list[tuple]): A list of tuples, each containing a command name and the time executed.

        Returns:
            str: The determined build strategy or an error message if the race is not recognized.
        """
        economy_commands = (
            {}
        )  # Placeholder for economy-related command values (to be populated)
        non_economy_commands = (
            {}
        )  # Placeholder for non-economy-related command values (to be populated)
        economy_resources = 0  # Total resources allocated to economy
        non_economy_resources = 0  # Total resources allocated to non-economy

        relevant_commands = []  # Commands executed within the relevant time frame

        # Filter commands based on time and relevance to economy/non-economy
        for command in commands:
            command_name, time = command
            if time > 5.30:  # Stop processing commands after 5 minutes and 30 seconds
                break
            if command_name in economy_commands or command_name in non_economy_commands:
                relevant_commands.append(command_name)

        # Calculate resources allocated to economy and non-economy
        for command in relevant_commands:
            if command in economy_commands:
                economy_resources += economy_commands[command]
            else:
                non_economy_resources += non_economy_commands[command]

        # Determine the build for the specified race based on calculated resources
        for race_type in self.race_types:
            if race == str(race_type):
                return race_type.get_build(economy_resources, non_economy_resources)

        print(
            "ERROR: data_analysis_tools\sc2\sc2_build_order\sc2_determine_build.py determine_build"
        )

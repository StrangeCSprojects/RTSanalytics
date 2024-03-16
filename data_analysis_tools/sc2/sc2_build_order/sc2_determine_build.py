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

    def determine_build(self, race: str, commands: list[tuple[tuple[str,str],int]]) -> str:
        """
        Determines the build based on the race and a list of commands executed in the game.
        Filters commands relevant to the economy and non-economy aspects up to 5 minutes and 30 seconds,
        then calculates resources allocated to each aspect to decide on the build strategy.

        Parameters:
            race (str): The race for which to determine the build (Zerg, Protoss, or Terran).
            commands (list[tuple[tuple[command_type, command_name],time]])): A list of tuples, each containing a tuple (command type, command name) and the time executed.

        Returns:
            str: The determined build strategy or an error message if the race is not recognized.
        """
        # Keys: Tuple[event.name, event.unit.name]
        # Values: resource cost
        economy_commands = (
            {
                ("UnitBornEvent", "SCV"): 50,
                ("UnitBornEvent", "Probe"): 50,
                ("UnitBornEvent", "Drone"): 50,
                ("UnitInitEvent", "CommandCenter"): 400,
                ("UnitInitEvent", "OrbitalCommand"): 400,              
                ("UnitInitEvent", "Nexus"): 400,
                ("UnitInitEvent", "Hatchery"): 300,
                ("UnitInitEvent", "Refinery"): 75,
                ("UnitInitEvent", "Assimilator"): 75,
                ("UnitInitEvent", "Extractor"): 25,
                ("UnitTypeChangeEvent", "OrbitalCommand"): 150,    
            }
        )  # Placeholder for economy-related command values (to be populated)
        non_economy_commands = (
            {    # Terran Units
                ("UnitBornEvent", "Marine"): 50,
                ("UnitBornEvent", "Marauder"): 125,
                ("UnitBornEvent", "Reaper"): 100,
                ("UnitBornEvent", "Ghost"): 275,
                ("UnitBornEvent", "Hellion"): 100,
                ("UnitBornEvent", "Hellbat"): 100,
                ("UnitBornEvent", "SiegeTank"): 275,
                ("UnitBornEvent", "Cyclone"): 175,
                ("UnitBornEvent", "WidowMine"): 100,
                ("UnitBornEvent", "Thor"): 500,
                ("UnitBornEvent", "Viking"): 225,
                ("UnitBornEvent", "Medivac"): 200,
                ("UnitBornEvent", "Liberator"): 275,
                ("UnitBornEvent", "Raven"): 250,
                ("UnitBornEvent", "Banshee"): 250,
                ("UnitBornEvent", "Battlecruiser"): 700,

                # Terran Buildings
                ("UnitInitEvent", "SupplyDepot"): 100,
                ("UnitInitEvent", "SupplyDepotLowered"): 100,
                ("UnitInitEvent", "Barracks"): 150,
                ("UnitInitEvent", "EngineeringBay"): 125,
                ("UnitInitEvent", "Bunker"): 100,
                ("UnitInitEvent", "MissileTurret"): 100,
                ("UnitInitEvent", "SensorTower"): 225,
                ("UnitInitEvent", "GhostAcademy"): 200,
                ("UnitInitEvent", "Factory"): 250,
                ("UnitInitEvent", "Starport"): 250,
                ("UnitInitEvent", "Armory"): 250,
                ("UnitInitEvent", "FusionCore"): 300,

                # Terran Infantry Weapon Upgrades
                ("UpgradeCompleteEvent", "TerranInfantryWeaponsLevel1"): 200,
                ("UpgradeCompleteEvent", "TerranInfantryWeaponsLevel2"): 350,
                ("UpgradeCompleteEvent", "TerranInfantryWeaponsLevel3"): 500,

                # Terran Infantry Armor Upgrades
                ("UpgradeCompleteEvent", "TerranInfantryArmorsLevel1"): 200,
                ("UpgradeCompleteEvent", "TerranInfantryArmorsLevel2"): 350,
                ("UpgradeCompleteEvent", "TerranInfantryArmorsLevel3"): 500,

                # Terran Vehicle Weapon Upgrades
                ("UpgradeCompleteEvent", "TerranVehicleWeaponsLevel1"): 200,
                ("UpgradeCompleteEvent", "TerranVehicleWeaponsLevel2"): 350,
                ("UpgradeCompleteEvent", "TerranVehicleWeaponsLevel3"): 500,

                # Terran Ship Weapon Upgrades
                ("UpgradeCompleteEvent", "TerranShipWeaponsLevel1"): 200,
                ("UpgradeCompleteEvent", "TerranShipWeaponsLevel2"): 350,
                ("UpgradeCompleteEvent", "TerranShipWeaponsLevel3"): 500,

                # Terran Vechicle and Ship Armor Upgrades
                ("UpgradeCompleteEvent", "TerranVehicleAndShipArmorsLevel1"): 200,
                ("UpgradeCompleteEvent", "TerranVehicleAndShipArmorsLevel2"): 350,
                ("UpgradeCompleteEvent", "TerranVehicleAndShipArmorsLevel3"): 500,

                # Engineering Bay Upgrades
                ("UpgradeCompleteEvent", "HiSecAutoTracking"): 200,
                ("UpgradeCompleteEvent", "TerranBuildingArmor"): 300,

                # Ghost Academy Upgrades
                ("UpgradeCompleteEvent", "PersonalCloaking"): 300,

                # Barracks Upgrades
                ("UpgradeCompleteEvent", "ShieldWall"): 200,
                ("UpgradeCompleteEvent", "Stimpack"): 200,
                ("UpgradeCompleteEvent", "PunisherGrenades"): 100,

                # Factory Upgrades
                ("UpgradeCompleteEvent", "HighCapacityBarrels"): 200,
                ("UpgradeCompleteEvent", "DrillClaws"): 150,
                ("UpgradeCompleteEvent", "HurricaneThrusters"): 200,
                ("UpgradeCompleteEvent", "SmartServos"): 200,

                # Starport Upgrades
                ("UpgradeCompleteEvent", "BansheeCloak"): 200,
                ("UpgradeCompleteEvent", "BansheeSpeed"): 250,
                ("UpgradeCompleteEvent", "InterferenceMatrix"): 100,

                # Fusion Core 
                ("UpgradeCompleteEvent", "BattlecruiserEnableSpecializations"): 300,
                ("UpgradeCompleteEvent", "MedivacCaduceusReactor"): 200,
                ("UpgradeCompleteEvent", "LiberatorAGRangeUpgrade"): 300,
                
                # Building Upgrades
                ("UnitTypeChangeEvent", "PlanetaryFortress"): 150,    

            }
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

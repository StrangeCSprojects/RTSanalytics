from data_analysis_tools.sc2.sc2_build_order.sc2_build_type import (
    Aggressive,
    Standard,
    Economic,
)


class RaceBuilds:
    """
    A base class representing builds for a race in StarCraft II,
    encapsulating different build strategies such as std, Aggressive, and eco.
    Each build type is associated with ranges of econ and non-econ resources.
    """

    def __init__(
        self,
        name,
        min_econ_std,
        max_econ_std,
        min_non_econ_std,
        max_non_econ_std,
        min_econ_aggr,
        max_econ_aggr,
        min_non_econ_aggr,
        max_non_econ_aggr,
        min_econ_eco,
        max_econ_eco,
        min_non_econ_eco,
        max_non_econ_ecnomic,
    ) -> None:
        """
        Initializes the RaceBuilds object with specific resource ranges for each build type.

        Parameters:
            - name: The name of the race.
            - min_econ_std, max_econ_std, etc.: Resource range parameters
              for each build type, specifying the minimum and maximum values of econ and non-econ
              resources that define the build.
        """
        self.name = name
        self.std_build = Standard(
            min_econ_std, max_econ_std, min_non_econ_std, max_non_econ_std
        )
        self.aggr_build = Aggressive(
            min_econ_aggr, max_econ_aggr, min_non_econ_aggr, max_non_econ_aggr
        )
        self.eco_build = Economic(
            min_econ_eco, max_econ_eco, min_non_econ_eco, max_non_econ_ecnomic
        )

    def get_build(self, econ_resources, non_econ_resources) -> str:
        """
        Determines the build type based on the provided economy and non-economy resources.

        Parameters:
            - econ_resources: The amount of economy resources available.
            - non_econ_resources: The amount of non-economy resources available.

        Returns:
            - A string representing the build type that matches the provided resources.
        """
        # std build checks
        if self.std_build.min_econ <= econ_resources <= self.std_build.max_econ:
            if (
                self.std_build.min_non_econ
                <= non_econ_resources
                <= self.std_build.max_non_econ
            ):
                return f"{self.std_build} {self}"

        # Aggressive build checks
        elif self.aggr_build.min_econ <= econ_resources <= self.aggr_build.max_econ:
            if (
                self.aggr_build.min_non_econ
                <= non_econ_resources
                <= self.aggr_build.max_non_econ
            ):
                return f"{self.aggr_build} {self}"


        # eco build checks
        elif self.eco_build.min_econ <= econ_resources <= self.eco_build.max_econ:
            if (
                self.eco_build.min_non_econ
                <= non_econ_resources
                <= self.eco_build.max_non_econ
            ):
                return f"{self.eco_build} {self}"

        else:
            # No matching build
            print("ERROR: No matching build found in choose_build.")

        """
    Returns a string representation of the RaceBuilds object, primarily the race name.
    """

    def __str__(self) -> str:
        return self.name


class ZergBuilds(RaceBuilds):
    """
    Defines build strategies specific to the Zerg race, including standard, aggressive, and economic builds.
    Pre-defines resource range values unique to Zerg for determining build types.
    """

    def __init__(self) -> None:
        """Pre-defined resource range values for Zerg"""
        # Zerg Build Values at 5-6 Minutes
        min_econ_std = 2300
        max_econ_std = 3300
        min_non_econ_std = 1700
        max_non_econ_std = 2700

        min_econ_aggr = 1300
        max_econ_aggr = 2299
        min_non_econ_aggr = 2701
        max_non_econ_aggr = 3700

        min_econ_eco = 3301
        max_econ_eco = 4300
        min_non_econ_eco = 1200
        max_non_econ_eco = 1699

        name = "Zerg"
        super().__init__(
            name,
            min_econ_std,
            max_econ_std,
            min_non_econ_std,
            max_non_econ_std,
            min_econ_aggr,
            max_econ_aggr,
            min_non_econ_aggr,
            max_non_econ_aggr,
            min_econ_eco,
            max_econ_eco,
            min_non_econ_eco,
            max_non_econ_eco,
        )


class ProtossBuilds(RaceBuilds):
    """
    Defines build strategies specific to the Protoss race, including standard, aggressive, and economic builds.
    Pre-defines resource range values unique to Protoss for determining build types.
    """

    def __init__(self) -> None:
        """Pre-defined resource range values for Protoss"""
        # Protoss Build Values at 5-6 Minutes
        min_econ_std = 2200
        max_econ_std = 3200
        min_non_econ_std = 1600
        max_non_econ_std = 2600

        min_econ_aggr = 1200
        max_econ_aggr = 2201
        min_non_econ_aggr = 2601
        max_non_econ_aggr = 3600

        min_econ_eco = 3201
        max_econ_eco = 4200
        min_non_econ_eco = 800
        max_non_econ_eco = 1599

        name = "Protoss"
        super().__init__(
            name,
            min_econ_std,
            max_econ_std,
            min_non_econ_std,
            max_non_econ_std,
            min_econ_aggr,
            max_econ_aggr,
            min_non_econ_aggr,
            max_non_econ_aggr,
            min_econ_eco,
            max_econ_eco,
            min_non_econ_eco,
            max_non_econ_eco,
        )


class TerranBuilds(RaceBuilds):
    """
    Defines build strategies specific to the Terran race, including standard, aggressive, and economic builds.
    Pre-defines resource range values unique to Terran for determining build types.
    """

    def __init__(self) -> None:
        """Pre-defined resource range values for Terran"""
        # Terran Build Values at 5-6 Minutes
        min_econ_std = 2000
        max_econ_std = 3000
        min_non_econ_std = 1500
        max_non_econ_std = 2500

        min_econ_aggr = 1000
        max_econ_aggr = 1999
        min_non_econ_aggr = 2501
        max_non_econ_aggr = 3500

        min_econ_eco = 3001
        max_econ_eco = 4000
        min_non_econ_eco = 600
        max_non_econ_eco = 1499

        name = "Terran"
        super().__init__(
            name,
            min_econ_std,
            max_econ_std,
            min_non_econ_std,
            max_non_econ_std,
            min_econ_aggr,
            max_econ_aggr,
            min_non_econ_aggr,
            max_non_econ_aggr,
            min_econ_eco,
            max_econ_eco,
            min_non_econ_eco,
            max_non_econ_eco,
        )

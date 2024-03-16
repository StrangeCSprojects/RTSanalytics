import pytest
from data_analysis_tools.sc2.sc2_build_order.sc2_determine_build import SC2DetermineBuild

def test_determine_build():
    sc2_determine_build = SC2DetermineBuild()

    race_terran = "Terran"
    commands_std_terran = [
        # Economy resources: 2200
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
         (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitInitEvent", "CommandCenter"), 1),
        (("UnitInitEvent", "CommandCenter"), 1),
        (("UnitInitEvent", "CommandCenter"), 1),

        # Non-Economy resources: 1650
        (("UnitInitEvent", "Barracks"), 1),
        (("UnitInitEvent", "Barracks"), 1),
        (("UnitInitEvent", "Barracks"), 1),
        (("UnitInitEvent", "EngineeringBay"), 1),
        (("UnitInitEvent", "EngineeringBay"), 1),
        (("UnitInitEvent", "SupplyDepot"), 1),
        (("UnitInitEvent", "SupplyDepot"), 1),
        (("UnitInitEvent", "Factory"), 1),
        (("UnitInitEvent", "Factory"), 1),
        (("UnitInitEvent", "Factory"), 1),
]
    commands_aggr_terran = [
        # Economy resources: 1800
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
         (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitInitEvent", "CommandCenter"), 1),
        (("UnitInitEvent", "CommandCenter"), 1),

        # Non-Economy resources: 2750
        (("UnitInitEvent", "Barracks"), 1),
        (("UnitInitEvent", "Barracks"), 1),
        (("UnitInitEvent", "Barracks"), 1),
        (("UnitInitEvent", "EngineeringBay"), 1),
        (("UnitInitEvent", "EngineeringBay"), 1),
        (("UnitInitEvent", "SupplyDepot"), 1),
        (("UnitInitEvent", "SupplyDepot"), 1),
        (("UnitInitEvent", "SupplyDepot"), 1),
        (("UnitInitEvent", "SupplyDepot"), 1),
        (("UnitInitEvent", "SupplyDepot"), 1),
        (("UnitInitEvent", "SupplyDepot"), 1),
        (("UnitInitEvent", "SupplyDepot"), 1),
        (("UnitInitEvent", "SupplyDepot"), 1),
        (("UnitInitEvent", "Factory"), 1),
        (("UnitInitEvent", "Factory"), 1),
        (("UnitInitEvent", "Factory"), 1),
        (("UnitInitEvent", "Factory"), 1),
        (("UnitInitEvent", "Factory"), 1),
]
    commands_eco_terran = [
        # Economy resources: 3400
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
         (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitBornEvent", "SCV"), 1),
        (("UnitInitEvent", "CommandCenter"), 1),
        (("UnitInitEvent", "CommandCenter"), 1),
        (("UnitInitEvent", "CommandCenter"), 1),
        (("UnitInitEvent", "CommandCenter"), 1),
        (("UnitInitEvent", "CommandCenter"), 1),
        (("UnitInitEvent", "CommandCenter"), 1),

        # Non-Economy resources: 1150
        (("UnitInitEvent", "Barracks"), 1),
        (("UnitInitEvent", "Barracks"), 1),
        (("UnitInitEvent", "Barracks"), 1),
        (("UnitInitEvent", "EngineeringBay"), 1),
        (("UnitInitEvent", "EngineeringBay"), 1),
        (("UnitInitEvent", "SupplyDepot"), 1),
        (("UnitInitEvent", "SupplyDepot"), 1),
        (("UnitInitEvent", "Factory"), 1),
    ]

    race_protoss = "Protoss"
    commands_std_protoss = []
    commands_aggr_protoss = []
    commands_eco_protoss = []

    race_zerg = "Zerg"
    commands_std_zerg = []
    commands_aggr_zerg = []
    commands_eco_zerg = []

    assert(sc2_determine_build.determine_build(race_terran, commands_std_terran) == "Standard Terran")
    assert(sc2_determine_build.determine_build(race_terran, commands_aggr_terran) == "Aggressive Terran")
    assert(sc2_determine_build.determine_build(race_terran, commands_eco_terran) == "Economic Terran")


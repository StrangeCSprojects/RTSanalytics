import pytest
from data_analysis_tools.sc2.sc2_build_order.sc2_race_builds import (
    ZergBuilds,
    ProtossBuilds,
    TerranBuilds,
)


# Define a test function to assess the accuracy of the get_build method across different races.
def test_get_build():
    # Initialize instances for each race's build analysis.
    zerg_builds = ZergBuilds()
    protoss_builds = ProtossBuilds()
    terran_builds = TerranBuilds()

    # Define resource allocation thresholds for different build strategies.
    # Standard build: Balanced between economy and military.
    econ_resources_std = 2400
    non_econ_resources_std = 2000

    # Aggressive build: Prioritizes military spending over economy.
    econ_resources_aggr = 1563
    non_econ_resources_aggr = 2750

    # Economy build: Focuses on economic development over military.
    econ_resources_eco = 3700
    non_econ_resources_eco = 1300

    # Assert that the get_build method correctly identifies the build strategy for Zerg based on the resources allocated.
    assert (
        zerg_builds.get_build(econ_resources_std, non_econ_resources_std)
        == "Standard Zerg"
    )
    assert (
        zerg_builds.get_build(econ_resources_aggr, non_econ_resources_aggr)
        == "Aggressive Zerg"
    )
    assert (
        zerg_builds.get_build(econ_resources_eco, non_econ_resources_eco)
        == "Economic Zerg"
    )

    # Perform the same assertions for Protoss builds.
    assert (
        protoss_builds.get_build(econ_resources_std, non_econ_resources_std)
        == "Standard Protoss"
    )
    assert (
        protoss_builds.get_build(econ_resources_aggr, non_econ_resources_aggr)
        == "Aggressive Protoss"
    )
    assert (
        protoss_builds.get_build(econ_resources_eco, non_econ_resources_eco)
        == "Economic Protoss"
    )

    # Perform the same assertions for Terran builds.
    assert (
        terran_builds.get_build(econ_resources_std, non_econ_resources_std)
        == "Standard Terran"
    )
    assert (
        terran_builds.get_build(econ_resources_aggr, non_econ_resources_aggr)
        == "Aggressive Terran"
    )
    assert (
        terran_builds.get_build(econ_resources_eco, non_econ_resources_eco)
        == "Economic Terran"
    )

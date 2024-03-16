import pytest
from data_analysis_tools.general.winrates.winrate_build import WinrateBuild


def test_calculate_matchup_winrates():
    # Initialize an instance of WinrateBuild to test its functionality.
    winrate_build = WinrateBuild()

    # Define a list of tuples representing individual match outcomes.
    # Each tuple contains two competing builds followed by the winning build.
    matches = [
        # Aggressive Zerg vs Standard Terran x10
        ("Standard Terran", "Aggressive Zerg", "Standard Terran"),
        ("Standard Terran", "Aggressive Zerg", "Standard Terran"),
        ("Standard Terran", "Aggressive Zerg", "Aggressive Zerg"),
        ("Aggressive Zerg", "Standard Terran", "Standard Terran"),
        ("Standard Terran", "Aggressive Zerg", "Aggressive Zerg"),
        ("Standard Terran", "Aggressive Zerg", "Aggressive Zerg"),
        ("Aggressive Zerg", "Standard Terran", "Standard Terran"),
        ("Aggressive Zerg", "Standard Terran", "Standard Terran"),
        ("Aggressive Zerg", "Standard Terran", "Aggressive Zerg"),
        ("Standard Terran", "Aggressive Zerg", "Standard Terran"),
        # Economic Protoss vs Standard Zerg x10
        ("Economic Protoss", "Standard Zerg", "Economic Protoss"),
        ("Economic Protoss", "Standard Zerg", "Standard Zerg"),
        ("Economic Protoss", "Standard Zerg", "Standard Zerg"),
        ("Economic Protoss", "Standard Zerg", "Standard Zerg"),
        ("Standard Zerg", "Economic Protoss", "Economic Protoss"),
        ("Standard Zerg", "Economic Protoss", "Economic Protoss"),
        ("Economic Protoss", "Standard Zerg", "Standard Zerg"),
        ("Standard Zerg", "Economic Protoss", "Standard Zerg"),
        ("Standard Zerg", "Economic Protoss", "Economic Protoss"),
        ("Economic Protoss", "Standard Zerg", "Standard Zerg"),
        # Aggressive Terran vs Standard Protoss x10
        ("Aggressive Terran", "Standard Protoss", "Standard Protoss"),
        ("Standard Protoss", "Aggressive Terran", "Standard Protoss"),
        ("Standard Protoss", "Aggressive Terran", "Standard Protoss"),
        ("Standard Protoss", "Aggressive Terran", "Standard Protoss"),
        ("Aggressive Terran", "Standard Protoss", "Standard Protoss"),
        ("Standard Protoss", "Aggressive Terran", "Aggressive Terran"),
        ("Standard Protoss", "Aggressive Terran", "Aggressive Terran"),
        ("Aggressive Terran", "Standard Protoss", "Aggressive Terran"),
        ("Aggressive Terran", "Standard Protoss", "Aggressive Terran"),
        ("Aggressive Terran", "Standard Protoss", "Aggressive Terran"),
        # Standard Terran vs Economic Protoss x10
        ("Standard Terran", "Economic Protoss", "Economic Protoss"),
        ("Economic Protoss", "Standard Terran", "Economic Protoss"),
        ("Economic Protoss", "Standard Terran", "Economic Protoss"),
        ("Economic Protoss", "Standard Terran", "Economic Protoss"),
        ("Standard Terran", "Economic Protoss", "Economic Protoss"),
        ("Economic Protoss", "Standard Terran", "Economic Protoss"),
        ("Economic Protoss", "Standard Terran", "Economic Protoss"),
        ("Standard Terran", "Economic Protoss", "Standard Terran"),
        ("Standard Terran", "Economic Protoss", "Standard Terran"),
        ("Standard Terran", "Economic Protoss", "Standard Terran"),
        # Aggressive Protoss vs Economic Zerg x10
        ("Aggressive Protoss", "Economic Zerg", "Aggressive Protoss"),
        ("Aggressive Protoss", "Economic Zerg", "Aggressive Protoss"),
        ("Aggressive Protoss", "Economic Zerg", "Aggressive Protoss"),
        ("Aggressive Protoss", "Economic Zerg", "Aggressive Protoss"),
        ("Economic Zerg", "Aggressive Protoss", "Aggressive Protoss"),
        ("Economic Zerg", "Aggressive Protoss", "Aggressive Protoss"),
        ("Aggressive Protoss", "Economic Zerg", "Aggressive Protoss"),
        ("Economic Zerg", "Aggressive Protoss", "Aggressive Protoss"),
        ("Economic Zerg", "Aggressive Protoss", "Aggressive Protoss"),
        ("Aggressive Protoss", "Economic Zerg", "Aggressive Protoss"),
    ]

    # Define expected win rate results for specific matchups.
    aggr_zerg_vs_std_terran = 40
    eco_protoss_vs_std_zerg = 40
    aggr_terran_vs_std_protoss = 50
    std_terran_vs_eco_protoss = 30
    aggr_protoss_vs_eco_zerg = 100

    # Assert that the calculated win rates match the expected results for specific matchups.
    # Aggressive Zerg vs Standard Terran
    assert (
        winrate_build.calculate_matchup_winrates(matches)["Aggressive Zerg"][
            "Standard Terran"
        ]
        == aggr_zerg_vs_std_terran
    )
    # Economic Protoss vs Standard Zerg
    assert (
        winrate_build.calculate_matchup_winrates(matches)["Economic Protoss"][
            "Standard Zerg"
        ]
        == eco_protoss_vs_std_zerg
    )
    # Aggressive Terran vs Standard Protoss
    assert (
        winrate_build.calculate_matchup_winrates(matches)["Aggressive Terran"][
            "Standard Protoss"
        ]
        == aggr_terran_vs_std_protoss
    )
    # Standard Terran vs Economic Protoss
    assert (
        winrate_build.calculate_matchup_winrates(matches)["Standard Terran"][
            "Economic Protoss"
        ]
        == std_terran_vs_eco_protoss
    )
    # Aggressive Protoss vs Economic
    assert (
        winrate_build.calculate_matchup_winrates(matches)["Aggressive Protoss"][
            "Economic Zerg"
        ]
        == aggr_protoss_vs_eco_zerg
    )

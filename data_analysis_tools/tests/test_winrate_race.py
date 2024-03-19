import pytest
from data_analysis_tools.general.winrates.winrate_race import WinrateRace


# Define a test function to assess the calculate_matchup_winrates method of the WinrateRace class.
def test_calculate_matchup_winrates():
    # Initialize an instance of WinrateRace to test its functionality.
    winrate_race = WinrateRace()

    # Define a list of tuples representing individual match outcomes.
    # Each tuple contains two competing races followed by the winning race.
    matches = [
        ("Terran", "Zerg", "Terran"),
        ("Terran", "Zerg", "Terran"),
        ("Terran", "Zerg", "Zerg"),
        ("Zerg", "Terran", "Terran"),
        ("Terran", "Zerg", "Zerg"),
        ("Terran", "Zerg", "Zerg"),
        ("Zerg", "Terran", "Terran"),
        ("Zerg", "Terran", "Terran"),
        ("Zerg", "Terran", "Zerg"),
        ("Terran", "Zerg", "Terran"),
        ("Protoss", "Zerg", "Protoss"),
        ("Protoss", "Zerg", "Zerg"),
        ("Protoss", "Zerg", "Zerg"),
        ("Protoss", "Zerg", "Zerg"),
        ("Zerg", "Protoss", "Protoss"),
        ("Zerg", "Protoss", "Protoss"),
        ("Protoss", "Zerg", "Zerg"),
        ("Zerg", "Protoss", "Zerg"),
        ("Zerg", "Protoss", "Protoss"),
        ("Protoss", "Zerg", "Zerg"),
        ("Terran", "Protoss", "Protoss"),
        ("Protoss", "Terran", "Protoss"),
        ("Protoss", "Terran", "Protoss"),
        ("Protoss", "Terran", "Protoss"),
        ("Terran", "Protoss", "Protoss"),
        ("Protoss", "Terran", "Terran"),
        ("Protoss", "Terran", "Terran"),
        ("Terran", "Protoss", "Terran"),
        ("Terran", "Protoss", "Terran"),
        ("Terran", "Protoss", "Terran"),
    ]

    # Define expected win rate results for specific matchups.
    zerg_vs_terran_results = 40
    protoss_vs_zerg_results = 40
    terran_vs_protoss_results = 50

    # Assert that the calculated win rates match the expected results for specific matchups.
    # Zerg vs. Terran win rates
    assert (
        winrate_race.calculate_matchup_winrates(matches)["Zerg"]["Terran"]
        == zerg_vs_terran_results
    )
    # Protoss vs. Zerg win rates
    assert (
        winrate_race.calculate_matchup_winrates(matches)["Protoss"]["Zerg"]
        == protoss_vs_zerg_results
    )
    # Terran vs. Protoss win rates
    assert (
        winrate_race.calculate_matchup_winrates(matches)["Terran"]["Protoss"]
        == terran_vs_protoss_results
    )

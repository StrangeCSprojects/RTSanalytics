import pytest
from data_analysis_tools.sc2.sc2_analyzer import SC2Analyzer
import random
from typing import Callable


def create_player_name():
    """A generator function to yield random player names."""
    names_lyst = [
        "Alex",
        "Jordan",
        "Sam",
        "Pat",
        "Jamie",
        "Morgan",
        "Taylor",
        "Casey",
        "Smith",
        "Johnson",
        "Williams",
        "Brown",
        "Jones",
        "Miller",
        "Davis",
        "Wilson",
        "TheDestroyer",
        "QuickSilver",
        "Ninja",
        "Ghost",
        "Phoenix",
        "Shadow",
        "Vortex",
        "Blaze",
    ]
    name = random.choice(names_lyst)
    return name

def create_aggr_commands():
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
    return commands_aggr_terran

def create_std_commands():
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
    return commands_std_terran

def create_eco_commands():
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
    return commands_eco_terran

def create_id():
    player_id = random.randint(0, 9999999)
    return player_id

def create_game_record(build_type_one: Callable, build_type_two: Callable, player_one_win: bool):
    # Player one table
    player_one_id = create_id()
    player_one_name = create_player_name()

    # Player two table
    player_two_id = create_id()
    player_two_name = create_player_name()

    # Game table
    game_id = create_id()
    game_mode = "1v1"
    game_map = "Solaris LE"

    # Player one play table
    game_one_id = game_id
    player_one_id = player_one_id
    race_one = "Terran"
    winner_one = player_one_win
    commands_one = build_type_one()

    # Player two play table
    game_two_id = game_id
    player_two_id = player_two_id
    race_two = "Terran"
    winner_two = not winner_one
    commands_two = build_type_two()

    player_one_data = (player_one_id, player_one_name)
    player_two_data = (player_two_id, player_two_name)


    game_data = (game_id, game_mode, game_map)
    play_one_data = (
        game_one_id,
        player_one_id,
        race_one,
        winner_one,
        commands_one,
    )
    play_two_data = (
        game_two_id,
        player_two_id,
        race_two,
        winner_two,
        commands_two,
    )

    record = (
        player_one_data,
        player_two_data,
        game_data,
        play_one_data,
        play_two_data,
    )

    return record

def generate_std_vs_aggr_60():
    for i in range(10):
        if i < 6:
            yield create_game_record(create_std_commands, create_aggr_commands, True)
        else:
            yield create_game_record(create_std_commands, create_aggr_commands, False)

def generate_aggr_vs_eco_80():
    for i in range(10):
        if i < 8:
            yield create_game_record(create_aggr_commands, create_eco_commands, True)
        else:
            yield create_game_record(create_aggr_commands, create_eco_commands, False)

def generate_eco_vs_std_70():
    for i in range(10):
        if i < 7:
            yield create_game_record(create_eco_commands, create_std_commands, True)
        else:
            yield create_game_record(create_eco_commands, create_std_commands, False)



def test_winrate_build():
    pass


def test_winrate_race():
    pass

def main():
    for record in generate_std_vs_aggr_60():
        print(record)
        print()

if __name__ == "__main__":
    main()
import pytest
from data_analysis_tools.sc2.sc2_analyzer import SC2Analyzer
import random
from typing import Callable

from json import loads, dumps
from data_analysis_tools.sc2.sc2_data_retriever import SC2DataRetriever
from database_tools.sc2.sc2_database import SC2_DB


@pytest.fixture(scope="module")
def setup_database():
    # Initialize the test database
    SC2_DB.init("test_analyzer_db")
    yield  # Run the tests
    SC2_DB.engine.dispose()

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

def test_winrate_build(setup_database):
    games_list = []
    players_list = []
    plays_list = []

    for record in generate_std_vs_aggr_60():
        # print(record)
        # print()
        # print()
        player_one = record[0]
        player_two = record[1]
        game = record[2]


        play_one_raw = record[3]
        game_id, player_id, race, is_winner, commands = play_one_raw
        serialized_commands = dumps(commands)
        play_one = (game_id, player_id, race, is_winner, serialized_commands)


        play_two_raw = record[4]
        game_id, player_id, race, is_winner, commands = play_two_raw
        serialized_commands = dumps(commands)
        play_two = (game_id, player_id, race, is_winner, serialized_commands)

        players_list.append(player_one)
        players_list.append(player_two)

        games_list.append(game)

        plays_list.append(play_one)
        plays_list.append(play_two)

    for record in generate_aggr_vs_eco_80():
        player_one = record[0]
        player_two = record[1]
        game = record[2]

        play_one_raw = record[3]
        game_id, player_id, race, is_winner, commands = play_one_raw
        serialized_commands = dumps(commands)
        play_one = (game_id, player_id, race, is_winner, serialized_commands)


        play_two_raw = record[4]
        game_id, player_id, race, is_winner, commands = play_two_raw
        serialized_commands = dumps(commands)
        play_two = (game_id, player_id, race, is_winner, serialized_commands)

        players_list.append(player_one)
        players_list.append(player_two)

        games_list.append(game)

        plays_list.append(play_one)
        plays_list.append(play_two)

    for record in generate_eco_vs_std_70():
        player_one = record[0]
        player_two = record[1]
        game = record[2]

        play_one_raw = record[3]
        game_id, player_id, race, is_winner, commands = play_one_raw
        serialized_commands = dumps(commands)
        play_one = (game_id, player_id, race, is_winner, serialized_commands)


        play_two_raw = record[4]
        game_id, player_id, race, is_winner, commands = play_two_raw
        serialized_commands = dumps(commands)
        play_two = (game_id, player_id, race, is_winner, serialized_commands)

        players_list.append(player_one)
        players_list.append(player_two)

        games_list.append(game)

        plays_list.append(play_one)
        plays_list.append(play_two)

    SC2_DB.add_games(games_list)
    SC2_DB.add_players(players_list)
    SC2_DB.add_plays(plays_list)

    data_retriever = SC2DataRetriever(SC2_DB)
    
    analyzer = SC2Analyzer(data_retriever)

    assert analyzer.winrate_build()['Aggressive Terran'] == {'Standard Terran': 40, 'Economic Terran': 80}

    assert analyzer.winrate_build()['Standard Terran'] == {'Economic Terran': 30, 'Aggressive Terran': 60}

    assert analyzer.winrate_build()['Economic Terran'] == {'Aggressive Terran': 20, 'Standard Terran': 70}


def test_winrate_race():
    pass

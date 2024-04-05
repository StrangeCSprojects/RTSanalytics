import pytest
from data_analysis_tools.sc2.sc2_analyzer import SC2Analyzer
import random
from typing import Callable

from json import loads, dumps
from database_tools.sc2.sc2_replay_data_retriever import SC2ReplayDataRetriever
from database_tools.sc2.sc2_database import SC2ReplayDB


@pytest.fixture(scope="module")
def setup_database():
    """Creates a database file to be used for testing"""
    # Initialize the test database
    SC2ReplayDB.init("test_analyzer_db")
    yield  # Run the tests
    SC2ReplayDB.engine.dispose()


def create_player_name() -> str:
    """
    :return: a random name
    """
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


def create_aggr_commands() -> list[tuple[tuple[str, str], int]]:
    """
    :return: the list of commands that would qualify as an 'Aggressive Terran' build
    """
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


def create_std_commands() -> list[tuple[tuple[str, str], int]]:
    """
    :return: the list of commands that would qualify as an 'Standard Terran' build
    """
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


def create_eco_commands() -> list[tuple[tuple[str, str], int]]:
    """
    :return: the list of commands that would qualify as an 'Economic Terran' build
    """
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


def create_id() -> None:
    """
    :return: a random player id
    """
    player_id = random.randint(0, 9999999)
    return player_id


def create_game_record_build(
    build_type_one: Callable, build_type_two: Callable, player_one_win: bool
) -> tuple:
    """
    Creates a record that contains all of the information for a game that would be gathered from a replay.
    With the only variable in the record being the build types.

    Parameters:
        build_type_one: the type of build order player one uses
        build_type_two: the type of build order player two uses
        player_one_win: whether or not player one won the game

    :return: a tuple containing all the data required for a game

    """
    # Player one table
    player_one_id = create_id()
    player_one_name = create_player_name()
    player_one_data = (player_one_id, player_one_name)

    # Player two table
    player_two_id = create_id()
    player_two_name = create_player_name()
    player_two_data = (player_two_id, player_two_name)

    # Game table
    game_id = create_id()
    game_mode = "1v1"
    game_map = "Solaris LE"
    game_data = (game_id, game_mode, game_map)

    # Player one play table
    game_one_id = game_id
    player_one_id = player_one_id
    race_one = "Terran"
    winner_one = player_one_win
    commands_one = build_type_one()
    play_one_data = (
        game_one_id,
        player_one_id,
        race_one,
        winner_one,
        commands_one,
    )

    # Player two play table
    game_two_id = game_id
    player_two_id = player_two_id
    race_two = "Terran"
    winner_two = not winner_one
    commands_two = build_type_two()
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


def create_game_record_race(
    player_one_race: str, player_two_race: str, player_one_win: bool
) -> tuple:
    """
    Creates a record that contains all of the information for a game that would be gathered from a replay.
    With the only variable in each record being the race.

    Parameters:
        player_one_race: the type of race player one uses
        player_two_race: the type of race player two uses
        player_one_win: whether or not player one won the game

    :return: a tuple containing all the data required for a game

    """
    # Player one table
    player_one_id = create_id()
    player_one_name = create_player_name()
    player_one_data = (player_one_id, player_one_name)

    # Player two table
    player_two_id = create_id()
    player_two_name = create_player_name()
    player_two_data = (player_two_id, player_two_name)

    # Game table
    game_id = create_id()
    game_mode = "1v1"
    game_map = "Solaris LE"
    game_data = (game_id, game_mode, game_map)

    # Player one play table
    game_one_id = game_id
    player_one_id = player_one_id
    race_one = player_one_race
    winner_one = player_one_win
    commands_one = create_std_commands()
    play_one_data = (
        game_one_id,
        player_one_id,
        race_one,
        winner_one,
        commands_one,
    )

    # Player two play table
    game_two_id = game_id
    player_two_id = player_two_id
    race_two = player_two_race
    winner_two = not winner_one
    commands_two = create_std_commands()
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
    """
    Generates ten games of 'Standard Terran' vs 'Aggressive Terran'. 'Standard Terran' wins six of the ten games.
    """
    for i in range(10):
        if i < 6:
            yield create_game_record_build(
                create_std_commands, create_aggr_commands, True
            )
        else:
            yield create_game_record_build(
                create_std_commands, create_aggr_commands, False
            )


def generate_aggr_vs_eco_80():
    """
    Generates ten games of 'Aggressive Terran' vs 'Economic Terran'. 'Aggressive Terran' wins eight of the ten games.
    """
    for i in range(10):
        if i < 8:
            yield create_game_record_build(
                create_aggr_commands, create_eco_commands, True
            )
        else:
            yield create_game_record_build(
                create_aggr_commands, create_eco_commands, False
            )


def generate_eco_vs_std_70():
    """
    Generates ten games of 'Economic Terran' vs 'Standard Terran'. 'Economic Terran' wins seven of the ten games.
    """
    for i in range(10):
        if i < 7:
            yield create_game_record_build(
                create_eco_commands, create_std_commands, True
            )
        else:
            yield create_game_record_build(
                create_eco_commands, create_std_commands, False
            )


def generate_terran_vs_zerg_50():
    """
    Generates ten games of 'Terran' vs 'Zerg'. 'Terran' wins five of the ten games.
    """
    for i in range(10):
        if i < 5:
            yield create_game_record_race("Terran", "Zerg", True)
        else:
            yield create_game_record_race("Terran", "Zerg", False)


def generate_zerg_vs_protoss_30():
    """
    Generates ten games of 'Zerg' vs 'Protoss'. 'Zerg' wins three of the ten games.
    """
    for i in range(10):
        if i < 3:
            yield create_game_record_race("Zerg", "Protoss", True)
        else:
            yield create_game_record_race("Zerg", "Protoss", False)


def generate_protoss_vs_terran_90():
    """
    Generates ten games of 'Protoss' vs 'Terran'. 'Protoss' wins nine of the ten games.
    """
    for i in range(10):
        if i < 9:
            yield create_game_record_race("Protoss", "Terran", True)
        else:
            yield create_game_record_race("Protoss", "Terran", False)


# BEFORE RUNNING!!!
# Only one method can be tested at a time and the test_analyzer_db file at database_tools\test_db.db must be deleted before each test
# Only uncomment one test at a time!!!

# def test_winrate_build(setup_database) -> None:
#     """
#     Tests the winrate_build method from sc2_analyzer.py

#     Parameters:
#         setup_database: allows us to use the test database file, doesn't need to be called
#     """

#     # Lists that are used to fill database with dummy data
#     games_list = []
#     players_list = []
#     plays_list = []

#     # Fill lists with data from ten auto generated Standard Terran vs Aggressive Terran games
#     # Standard Terran wins 6/10 games
#     for record in generate_std_vs_aggr_60():

#         # Retrieve table specific data from record
#         player_one = record[0]
#         player_two = record[1]
#         game = record[2]

#         # List of commands need to be converted to json string to be stored in database
#         play_one_raw = record[3]
#         game_id, player_id, race, is_winner, commands = play_one_raw
#         serialized_commands = dumps(commands)
#         play_one = (game_id, player_id, race, is_winner, serialized_commands)

#         # List of commands need to be converted to json string to be stored in database
#         play_two_raw = record[4]
#         game_id, player_id, race, is_winner, commands = play_two_raw
#         serialized_commands = dumps(commands)
#         play_two = (game_id, player_id, race, is_winner, serialized_commands)

#         # Fill lists with 'game' data
#         players_list.append(player_one)
#         players_list.append(player_two)
#         games_list.append(game)
#         plays_list.append(play_one)
#         plays_list.append(play_two)

#     for record in generate_aggr_vs_eco_80():

#         # Retrieve table specific data from record
#         player_one = record[0]
#         player_two = record[1]
#         game = record[2]

#         # List of commands need to be converted to json string to be stored in database
#         play_one_raw = record[3]
#         game_id, player_id, race, is_winner, commands = play_one_raw
#         serialized_commands = dumps(commands)
#         play_one = (game_id, player_id, race, is_winner, serialized_commands)

#         # List of commands need to be converted to json string to be stored in database
#         play_two_raw = record[4]
#         game_id, player_id, race, is_winner, commands = play_two_raw
#         serialized_commands = dumps(commands)
#         play_two = (game_id, player_id, race, is_winner, serialized_commands)

#         # Fill lists with 'game' data
#         players_list.append(player_one)
#         players_list.append(player_two)
#         games_list.append(game)
#         plays_list.append(play_one)
#         plays_list.append(play_two)

#     for record in generate_eco_vs_std_70():

#         # Retrieve table specific data from record
#         player_one = record[0]
#         player_two = record[1]
#         game = record[2]

#         # List of commands need to be converted to json string to be stored in database
#         play_one_raw = record[3]
#         game_id, player_id, race, is_winner, commands = play_one_raw
#         serialized_commands = dumps(commands)
#         play_one = (game_id, player_id, race, is_winner, serialized_commands)

#         # List of commands need to be converted to json string to be stored in database
#         play_two_raw = record[4]
#         game_id, player_id, race, is_winner, commands = play_two_raw
#         serialized_commands = dumps(commands)
#         play_two = (game_id, player_id, race, is_winner, serialized_commands)

#         # Fill lists with 'game' data
#         players_list.append(player_one)
#         players_list.append(player_two)
#         games_list.append(game)
#         plays_list.append(play_one)
#         plays_list.append(play_two)

#     # Push lists to database
#     SC2_DB.add_games(games_list)
#     SC2_DB.add_players(players_list)
#     SC2_DB.add_plays(plays_list)

#     data_retriever = SC2DataRetriever(SC2_DB)

#     analyzer = SC2Analyzer(data_retriever)

#     # Assert Tests
#     assert analyzer.winrate_build()['Aggressive Terran'] == {'Standard Terran': 40, 'Economic Terran': 80}

#     assert analyzer.winrate_build()['Standard Terran'] == {'Economic Terran': 30, 'Aggressive Terran': 60}

#     assert analyzer.winrate_build()['Economic Terran'] == {'Aggressive Terran': 20, 'Standard Terran': 70}

# def test_winrate_race(setup_database) -> None:
#     """
#     Tests the winrate_race method from sc2_analyzer.py

#     Parameters:
#         setup_database: allows us to use the test database file, doesn't need to be called
#     """

#     # Lists that are used to fill database with dummy data
#     games_list = []
#     players_list = []
#     plays_list = []

#     # Fill lists with data from ten auto generated Terran vs Zerg games
#     # Terran wins 5/10 games
#     for record in generate_terran_vs_zerg_50():

#         # Retrieve table specific data from record
#         player_one = record[0]
#         player_two = record[1]
#         game = record[2]

#         # List of commands need to be converted to json string to be stored in database
#         play_one_raw = record[3]
#         game_id, player_id, race, is_winner, commands = play_one_raw
#         serialized_commands = dumps(commands)
#         play_one = (game_id, player_id, race, is_winner, serialized_commands)

#         # List of commands need to be converted to json string to be stored in database
#         play_two_raw = record[4]
#         game_id, player_id, race, is_winner, commands = play_two_raw
#         serialized_commands = dumps(commands)
#         play_two = (game_id, player_id, race, is_winner, serialized_commands)

#         # Fill lists with 'game' data
#         players_list.append(player_one)
#         players_list.append(player_two)
#         games_list.append(game)
#         plays_list.append(play_one)
#         plays_list.append(play_two)

#     for record in generate_zerg_vs_protoss_30():

#         # Retrieve table specific data from record
#         player_one = record[0]
#         player_two = record[1]
#         game = record[2]

#         # List of commands need to be converted to json string to be stored in database
#         play_one_raw = record[3]
#         game_id, player_id, race, is_winner, commands = play_one_raw
#         serialized_commands = dumps(commands)
#         play_one = (game_id, player_id, race, is_winner, serialized_commands)

#         # List of commands need to be converted to json string to be stored in database
#         play_two_raw = record[4]
#         game_id, player_id, race, is_winner, commands = play_two_raw
#         serialized_commands = dumps(commands)
#         play_two = (game_id, player_id, race, is_winner, serialized_commands)

#         # Fill lists with 'game' data
#         players_list.append(player_one)
#         players_list.append(player_two)
#         games_list.append(game)
#         plays_list.append(play_one)
#         plays_list.append(play_two)

#     for record in generate_protoss_vs_terran_90():

#         # Retrieve table specific data from record
#         player_one = record[0]
#         player_two = record[1]
#         game = record[2]

#         # List of commands need to be converted to json string to be stored in database
#         play_one_raw = record[3]
#         game_id, player_id, race, is_winner, commands = play_one_raw
#         serialized_commands = dumps(commands)
#         play_one = (game_id, player_id, race, is_winner, serialized_commands)

#         # List of commands need to be converted to json string to be stored in database
#         play_two_raw = record[4]
#         game_id, player_id, race, is_winner, commands = play_two_raw
#         serialized_commands = dumps(commands)
#         play_two = (game_id, player_id, race, is_winner, serialized_commands)

#         # Fill lists with 'game' data
#         players_list.append(player_one)
#         players_list.append(player_two)
#         games_list.append(game)
#         plays_list.append(play_one)
#         plays_list.append(play_two)

#     # Push lists to database
#     SC2_DB.add_games(games_list)
#     SC2_DB.add_players(players_list)
#     SC2_DB.add_plays(plays_list)

#     data_retriever = SC2DataRetriever(SC2_DB)

#     analyzer = SC2Analyzer(data_retriever)

#     # Assert Tests
#     assert analyzer.winrate_race()['Terran'] == {'Zerg': 50, 'Protoss': 10}

#     assert analyzer.winrate_race()['Zerg'] == {'Terran': 50, 'Protoss': 30}

#     assert analyzer.winrate_race()['Protoss'] == {'Terran': 90, 'Zerg': 70}

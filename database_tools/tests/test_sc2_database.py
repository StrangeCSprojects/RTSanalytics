import pytest
from sqlalchemy.orm import declarative_base
from database_tools.sc2_database import SC2_DB


Base = declarative_base()  # Define Base using declarative_base() from sqlalchemy.orm


# Fixture to set up and tear down the database connection for each test
@pytest.fixture(scope="module")
def setup_database():
    # Initialize the test database
    SC2_DB.init("test_db")
    yield  # Run the tests
    SC2_DB.engine.dispose()


# Test cases
def test_add_plays(setup_database):
    # Create a list of play data
    plays = [
        (1, 1, "Terran", True, "command1"),
        (1, 2, "Protoss", False, "command2"),
    ]
    # Add plays to the database
    SC2_DB.add_plays(plays)
    # Retrieve all plays from the database
    all_plays = SC2_DB.get_all_plays()
    # Check if the plays were added correctly
    assert all_plays == tuple(plays)


def test_get_player_by_name(setup_database):
    # Add a player to the database
    player_id, player_name = 1, "Player1"
    SC2_DB.add_players([(player_id, player_name)])
    # Retrieve the player by name
    retrieved_player = SC2_DB.get_player_by_name(player_name)
    # Check if the player was retrieved correctly
    assert retrieved_player == (player_id, player_name)


def test_get_player_by_id(setup_database):
    # Add a player to the database
    player_id, player_name = 1, "Player1"
    SC2_DB.add_players([(player_id, player_name)])
    # Retrieve the player by id
    retrieved_player = SC2_DB.get_player_by_id(player_id)
    # Check if the player was retrieved correctly
    assert retrieved_player == (player_id, player_name)


def test_get_players_in_game(setup_database):
    # Add players and plays to the database
    players = [(1, "Player1"), (2, "Player2")]
    plays = [(1, 1, "Terran", True, "command1"), (1, 2, "Protoss", False, "command2")]
    SC2_DB.add_players(players)
    SC2_DB.add_plays(plays)
    # Retrieve players in a game
    players_in_game = SC2_DB.get_players_in_game(1)
    # Check if the players in the game were retrieved correctly
    assert players_in_game == ((1, "Player1"), (2, "Player2"))


def test_get_play(setup_database):
    # Add plays to the database
    plays = [(1, 1, "Terran", True, "command1"), (1, 2, "Protoss", False, "command2")]
    SC2_DB.add_plays(plays)
    # Retrieve a play
    game_id, player_id, race, winner, commands = SC2_DB.get_play(1, 1)
    # Check if the play was retrieved correctly
    assert (race, winner, commands) == ("Terran", True, "command1")


def test_get_all_players(setup_database):
    # Add players to the database
    players = [(1, "Player1"), (2, "Player2")]
    SC2_DB.add_players(players)
    # Retrieve all players
    all_players = SC2_DB.get_all_players()
    # Check if all players were retrieved correctly
    assert all_players == tuple(players)


def test_get_all_games(setup_database):
    # Add games to the database
    games = [(1, "Mode1", "Map1"), (2, "Mode2", "Map2")]
    SC2_DB.add_games(games)
    # Retrieve all games
    all_games = SC2_DB.get_all_games()
    # Check if all games were retrieved correctly
    assert all_games == tuple(games)

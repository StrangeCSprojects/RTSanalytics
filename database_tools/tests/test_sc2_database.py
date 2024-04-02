import pytest
from sqlalchemy.orm import declarative_base
from database_tools.sc2.sc2_database import SC2_DB
from database_tools.sc2.entities.sc2_db_entities import Play, Player, Game


Base = declarative_base()  # Define Base using declarative_base() from sqlalchemy.orm


# Fixture to set up and tear down the database connection for each test
@pytest.fixture()
def setup_database(scope="module"):
    # Initialize the test database
    SC2_DB.init("test_db")
    yield  # Run the tests
    # Clean the data from relevant tables after all tests are finished
    with SC2_DB.Session() as session:
        session.query(Game).delete()
        session.query(Player).delete()
        session.query(Play).delete()
        session.commit()
    # Close the database connection after cleaning
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
    with SC2_DB.Session() as session:
        session.query(Play).delete()


def test_add_players(setup_database):
    # Create a list of player data
    players = [
        (1, "p1"),
        (2, "p2"),
    ]
    # Add players to the database
    SC2_DB.add_players(players)
    # Retrieve all players from the database
    all_players = SC2_DB.get_all_players()
    # Check if the players were added correctly
    assert all_players == tuple(players)
    with SC2_DB.Session() as session:
        session.query(Player).delete()


def test_add_games(setup_database):
    # Create a list of game data
    games = [
        (1, "mode1", "map1"),
        (2, "mode2", "map2"),
    ]
    # Add games to the database
    SC2_DB.add_games(games)
    # Retrieve all games from the database
    all_games = SC2_DB.get_all_games()
    # Check if the games were added correctly
    assert all_games == tuple(games)
    with SC2_DB.Session() as session:
        session.query(Game).delete()


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
    race, winner, commands = SC2_DB.get_play(1, 1)
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
    assert len(all_games) == len(games)

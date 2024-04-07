import pytest
from unittest.mock import Mock
from database_tools.sc2.sc2_data_retriever import SC2DataRetriever


@pytest.fixture(scope="module")
def setup_database():
    # Set up mock database
    database_mock = Mock()
    database_mock.get_play.return_value = ("Terran", True, "command1")
    database_mock.get_all_players.return_value = [(1, "Player1"), (2, "Player2")]
    database_mock.get_all_games.return_value = [(1, "Map1", "Mode1"), (2, "Map2", "Mode2")]

    yield database_mock


def test_get_play(setup_database):
    # Initialize SC2DataRetriever with mock database
    data_retriever = SC2DataRetriever(setup_database)

    # Test getting play data
    game_id = 1
    player_id = 1
    play_data = data_retriever.get_play(game_id, player_id)

    # Assert expected play data
    assert play_data == ("Terran", True, "command1")


def test_get_all_players(setup_database):
    # Initialize SC2DataRetriever with mock database
    data_retriever = SC2DataRetriever(setup_database)

    # Test getting all players
    all_players = data_retriever.get_all_players()

    # Assert expected player data
    assert all_players == [(1, "Player1"), (2, "Player2")]


def test_get_all_games(setup_database):
    # Initialize SC2DataRetriever with mock database
    data_retriever = SC2DataRetriever(setup_database)

    # Test getting all games
    all_games = data_retriever.get_all_games()

    # Assert expected game data
    assert all_games == [(1, "Map1", "Mode1"), (2, "Map2", "Mode2")]

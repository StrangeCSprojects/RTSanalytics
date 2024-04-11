import pytest
from database_tools.sc2.sc2_replay_data_retriever import SC2ReplayDataRetriever
from database_tools.sc2.sc2_replay_database import SC2ReplayDB
from database_tools.sc2.entities.sc2_replay_entities import (
    Play,
    Player,
    Game
)


@pytest.fixture(scope="module")
def setup_database(scope="module"):
    # Set up mock database
    SC2ReplayDB.init("test_replay_db")
    SC2ReplayDB.add_plays(
        [
            (1, 1, "Terran", True, "command1"),
            (2, 4, "Zerg", False, "command2")
        ]
    )
    SC2ReplayDB.add_players(
        [
            (1, "Player1"),
            (2, "Player2")
        ]
    )
    SC2ReplayDB.add_games(
        [
            (1, "Map1", "Mode1"),
            (2, "Map2", "Mode2")
        ]
    )
    yield # Run the tests
    with SC2ReplayDB.Session() as session:
        session.query(Game).delete()
        session.query(Player).delete()
        session.query(Play).delete()
        session.commit()
    # Close the connection to the test database
    SC2ReplayDB.engine.dispose()


def test_get_play(setup_database):
    # Initialize SC2DataRetriever with mock database
    data_retriever = SC2ReplayDataRetriever(SC2ReplayDB)

    # Test getting play data
    game_id = 1
    player_id = 1
    play_data = data_retriever.get_play(game_id, player_id)

    # Assert expected play data
    assert play_data == ("Terran", True, "command1")


def test_get_all_players(setup_database):
    # Initialize SC2DataRetriever with mock database
    data_retriever = SC2ReplayDataRetriever(SC2ReplayDB)

    # Test getting all players
    all_players = data_retriever.get_all_players()

    # Assert expected player data
    assert all_players == ((1, "Player1"), (2, "Player2"))


def test_get_all_games(setup_database):
    # Initialize SC2DataRetriever with mock database
    data_retriever = SC2ReplayDataRetriever(SC2ReplayDB)

    # Test getting all games
    all_games = data_retriever.get_all_games()

    # Assert expected game data
    assert all_games == ((1, "Map1", "Mode1"), (2, "Map2", "Mode2"))

import pytest
from database_tools.sc2.sc2_replay_database import SC2ReplayDB
from database_tools.sc2.entities.sc2_replay_entities import Play, Player, Game
from database_tools.sc2.sc2_database_access import (
    PlayDataStorage,
    PlayerDataStorage,
    GameDataStorage,
)


# Fixture to set up and tear down the database connection for each test
@pytest.fixture(scope="module")
def setup_database(scope="module"):
    # Set up test database
    SC2ReplayDB.init("test_db")
    yield # Run the tests
    # Clean the data from the tables once the tests are finished
    with SC2ReplayDB.Session() as session:
        session.query(Game).delete()
        session.query(Player).delete()
        session.query(Play).delete()
        session.commit()
    # Close the database connection after cleaning
    SC2ReplayDB.engine.dispose()


def test_push_play_data(setup_database):
    # Initialize PlayDataStorage
    play_storage = PlayDataStorage()
    play_data = (1, 1, "Terran", True, "command1")
    play_storage.set_data(play_data)

    # Push the data to the database
    play_storage.push()

    # Check if the data was added to the database
    with SC2ReplayDB.Session() as session:
        play = session.query(Play).filter_by(game_id=1, player_id=1).first()
        assert play is not None
        assert play.race == "Terran"
        assert play.winner == True
        assert play.commands == '"command1"'

    # Attempt to push the same game data again
    play_storage.push()

    # Check if the play data was added only once
    with SC2ReplayDB.Session() as session:
        num_plays = session.query(Play).filter_by(game_id=1, player_id=1).count()

    assert num_plays == 1


def test_push_player_data(setup_database):
    # Initialize PlayerDataStorage
    player_storage = PlayerDataStorage()
    player_data = (1, "Player1")

    # Push the data to the database
    player_storage.set_data(player_data)
    player_storage.push()

    # Check if the data was added to the database
    with SC2ReplayDB.Session() as session:
        player = session.query(Player).filter_by(player_id=1, name="Player1").first()
        assert player is not None

    # Attempt to push the same game data again
    player_storage.push()

    # Check if the player data was added only once
    with SC2ReplayDB.Session() as session:
        num_players = session.query(Player).filter_by(player_id=1).count()

    assert num_players == 1


def test_push_game_data(setup_database):
    # Initialize test data
    game_storage = GameDataStorage()
    game_data = (1, "Map1", "Mode1")

    # Add game data to the database
    game_storage.set_data(game_data)
    game_storage.push()

    # Check if the data was added to the database
    with SC2ReplayDB.Session() as session:
        game = session.query(Game).filter_by(game_id=1)
        assert game is not None

    # Attempt to push the same game data again
    game_storage.push()

    # Check if the game data was added only once
    with SC2ReplayDB.Session() as session:
        num_games = session.query(Game).filter_by(game_id=1).count()

    assert num_games == 1

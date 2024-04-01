import pytest
import os

from sc2reader.objects import Player
from database_tools.entities.sc2_db_entities import Game, Play, Player
from database_tools.sc2.sc2_database import SC2_DB
from replay_extraction_tools.sc2.sc2_extractor import SC2Extractor


@pytest.fixture(scope="module")
def setup_sc2_extractor():
    # Set up fixture
    extractor = SC2Extractor()
    extractor.folder_path = "replay_extraction_tools/replays"
    SC2_DB.init("test_extractor_db")
    yield extractor
    # Clean the data from relevant tables after all tests are finished
    with SC2_DB.Session() as session:
        session.query(Game).delete()
        session.query(Player).delete()
        session.query(Play).delete()
        session.commit()
    # Close the database connection after cleaning
    SC2_DB.engine.dispose()


def test_extract_and_filter(setup_sc2_extractor):
    # Check if the provided replay folder path contains any StarCraft II replay files
    contains_replays = any(
        filename.endswith(".SC2Replay")
        for filename in os.listdir(setup_sc2_extractor.folder_path)
    )

    # Call the extract method
    replay_container = setup_sc2_extractor.extract()

    if contains_replays:
        # Assert that replay container is not empty if replay files exist in the folder
        assert replay_container
    else:
        # Assert that replay container is empty if no replay files exist in the folder
        assert not replay_container
        return  # No need to further test this folder path

    # Call the filter function
    setup_sc2_extractor.filter_into_tables(replay_container)

    # Check for correct number of players and games
    assert (
        setup_sc2_extractor._player_data.get_length() == 6
    )  # SC2_DB eliminates duplicate players
    assert (
        setup_sc2_extractor._game_data.get_length() == 3
    )  # 4 games - 1 ("gathering resources" game)
    assert (
        setup_sc2_extractor._play_data.get_length()
        == 2 * setup_sc2_extractor._game_data.get_length()
    )


def test_run(setup_sc2_extractor):
    # Call the run method
    replay_folder_path = setup_sc2_extractor.folder_path
    setup_sc2_extractor.run(replay_folder_path)

    # Now check if duplicate games/players have been removed in database
    with SC2_DB.Session() as session:
        assert session.query(Player).count() == 4
        # assert session.query(Play).count() == 2 * session.query(Game).count()
        # assert session.query(Game).count() == 3
        
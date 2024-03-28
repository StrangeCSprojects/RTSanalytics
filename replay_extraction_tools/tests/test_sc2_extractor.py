import pytest
import os
from replay_extraction_tools.sc2.sc2_extractor import SC2Extractor


@pytest.fixture
def setup_sc2_extractor():
    # Set up fixture
    extractor = SC2Extractor()
    replay_folder_path = "replay_extraction_tools\\replays"
    extractor.folder_path = replay_folder_path
    yield extractor


def test_extract(setup_sc2_extractor):
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


# def test_filter_into_tables(setup_sc2_extractor):
#     # Get replay data from replay folder
#     replay_container = setup_sc2_extractor.extract()

#     # Call the filter_into_tables method
#     setup_sc2_extractor.filter_into_tables(replay_container)

    # TODO:
    #
    # CREATE "DUMMY" REPLAY CONTAINER (DON'T CALL EXTRACT METHOD AND GETT REAL DATA)
    # NEED TO CHECK IF ANY GAMES WITHOUT A WINNER HAVE BEEN STORED
    # NEED TO CHECK IF ANY GAMES WITH NUMBER OF PLAYERS NOT EQUAL TO 2
    # NEED TO CHECK THAT COMMAND DATA IS PROPERLY SORTED INTO LISTS
    # NEED TO CHECK THAT, NO MATTER WHAT, EACH GAME HAS ONE WINNER AND LOSER
    #
    # NO NEED TO CHECK ANYTHING ELSE SINCE ALL DEPENDENCIES HAVE BEEN TESTED


# FINISH THIS TEST LATER
# def test_run(setup_sc2_extractor, tmpdir):
#     # Set up test data
#     replay_folder_path = tmpdir.mkdir("replays")
#     # Create mock replay files in the temporary directory

#     # Call the run method
#     setup_sc2_extractor.run(replay_folder_path)

#     # Assert any necessary conditions based on the behavior of the method

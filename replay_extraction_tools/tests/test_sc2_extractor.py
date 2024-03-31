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

    # Call the filter function
    setup_sc2_extractor.filter_into_tables(replay_container)


# Finish this test later
def test_run(setup_sc2_extractor):
    # Set up test data
    replay_folder_path = tmpdir.mkdir("replays")
    # Create mock replay files in the temporary directory

    # Call the run method
    setup_sc2_extractor.run(replay_folder_path)

    # Assert any necessary conditions based on the behavior of the method

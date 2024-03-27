import pytest
import os
from replay_extraction_tools.sc2.sc2_extractor import SC2Extractor

@pytest.fixture
def sc2_extractor():
    # Set up any necessary fixtures
    extractor = SC2Extractor()
    yield extractor
    # Teardown, if needed

def test_extract(sc2_extractor):
    # Set up test data
    replay_folder_path = "replay_extraction_tools/replays/"
    sc2_extractor.replay_folder_path = replay_folder_path
    
    # Check if the provided replay folder path contains any StarCraft II replay files
    contains_replays = any(filename.endswith('.SC2Replay') for filename in os.listdir(replay_folder_path))
    
    # Call the extract method
    replay_container = sc2_extractor.extract()
    
    if contains_replays:
        # Assert that replay container is not empty if replay files exist in the folder
        assert replay_container
    else:
        # Assert that replay container is empty if no replay files exist in the folder
        assert not replay_container

def test_filter_into_tables(sc2_extractor):
    # Set up test data
    replay_container = {1: "mock_replay_data"}
    
    # Call the filter_into_tables method
    sc2_extractor.filter_into_tables(replay_container)
    
    # Assert any necessary conditions based on the behavior of the method

# You can add more test cases as needed

def test_run(sc2_extractor, tmpdir):
    # Set up test data
    replay_folder_path = tmpdir.mkdir("replays")
    # Create mock replay files in the temporary directory
    
    # Call the run method
    sc2_extractor.run(replay_folder_path)
    
    # Assert any necessary conditions based on the behavior of the method

import pytest
import os
from sc2_major_battles_extractor import SC2MajorBattlesExtractor
from database_tools.general.general_database_access import DataStorage

@pytest.fixture(scope="module")
def setup_sc2_major_battles_extractor():
    """
    Fixture to set up the SC2MajorBattlesExtractor instance for testing.
    It initializes the extractor and sets the folder path to a test directory containing replay files.
    """
    extractor = SC2MajorBattlesExtractor()
    extractor.folder_path = "path_to_test_replay_files"
    yield extractor
    # Clean up any resources if necessary

def test_extract_replays(setup_sc2_major_battles_extractor):
    """
    Test the extract method of SC2MajorBattlesExtractor.

    This test verifies that the extract method correctly processes replay files in the specified folder.
    - If replay files are present, the method should return a non-empty dictionary of replay data.
    - If no replay files are present, the method should return an empty dictionary.
    """
    # Check if the provided replay folder path contains any StarCraft II replay files
    contains_replays = any(
        filename.endswith(".SC2Replay")
        for filename in os.listdir(setup_sc2_major_battles_extractor.folder_path)
    )

    # Call the extract method
    replay_container = setup_sc2_major_battles_extractor.extract()

    if contains_replays:
        # Assert that replay container is not empty if replay files exist in the folder
        assert replay_container
    else:
        # Assert that replay container is empty if no replay files exist in the folder
        assert not replay_container

def test_unit_death_data_extraction(setup_sc2_major_battles_extractor):
    """
    Test the extraction of unit death data.

    This test ensures that the extract method includes unit death data in the replay data.
    - The replay data should contain a 'unit_deaths' key.
    - The value associated with 'unit_deaths' should be a list (or other appropriate data structure).
    """
    # Extract data from replays
    replay_container = setup_sc2_major_battles_extractor.extract()
    
    # Verify that the unit death data is correctly populated
    for replay_data in replay_container.values():
        assert 'unit_deaths' in replay_data
        assert isinstance(replay_data['unit_deaths'], list)  # or another suitable type based on implementation

def test_batch_insert_unit_death_data(setup_sc2_major_battles_extractor):
    """
    Test the insertion of unit death data into the database.

    This test verifies that the extracted unit death data is correctly inserted into the database.
    - The test checks that the database contains the expected number of unit death records after insertion.
    - Adjust the assertions based on your database schema and expected outcomes.
    """
    # Extract data from replays
    replay_container = setup_sc2_major_battles_extractor.extract()

    # Assuming there is a method similar to _batch_insert that inserts data into a database
    setup_sc2_major_battles_extractor.insert_into_database(replay_container)

    # Here you would write assertions that validate data was correctly inserted into your database
    # For example, checking that counts in relevant tables match expectations
    with SC2ReplayDB.Session() as session:
        unit_death_count = session.query(UnitDeathData).count()
        assert unit_death_count > 0  # Or another appropriate check

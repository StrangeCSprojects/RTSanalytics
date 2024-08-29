import pytest
import os
from replay_extraction_tools.sc2.sc2_major_battles_extractor import (
    SC2MajorBattlesExtractor,
)  # Import SC2MajorBattlesExtractor for extracting replay data.
from database_tools.sc2.sc2_major_battle_access import (
    UnitDeathDataStorage,
)  # Import UnitDeathDataStorage for managing unit death data.
from database_tools.sc2.entities.sc2_major_battle_entities import (
    UnitDeath,
)  # Import ORM entity for unit death.
from database_tools.sc2.sc2_major_battle_database import (
    SC2MajorBattleDB,
)  # Import SC2MajorBattleDB for database operations.


@pytest.fixture(scope="module")
def setup_sc2_major_battles_extractor():
    """
    Fixture to set up the SC2MajorBattlesExtractor instance for testing.
    Initializes the extractor and sets the folder path to a test directory containing replay files.
    """
    extractor = (
        SC2MajorBattlesExtractor()
    )  # Create an instance of SC2MajorBattlesExtractor.
    extractor.folder_path = "replay_extraction_tools/replays"  # Set the folder path to the directory with replay files.
    yield extractor
    # Clean up resources if necessary (not required for this in-memory setup).


def test_extract_replays(setup_sc2_major_battles_extractor):
    """
    Test the extract method of SC2MajorBattlesExtractor.

    Verifies that the extract method correctly processes replay files in the specified folder.
    - If replay files are present, the method should return a non-empty dictionary of replay data.
    - If no replay files are present, the method should return an empty dictionary.
    """
    # Check if the provided replay folder path contains any StarCraft II replay files.
    contains_replays = any(
        filename.endswith(".SC2Replay")
        for filename in os.listdir(setup_sc2_major_battles_extractor.folder_path)
    )

    # Call the extract method to process the replay files.
    replay_container = setup_sc2_major_battles_extractor.extract()

    if contains_replays:
        # Assert that replay container is not empty if replay files exist in the folder.
        assert replay_container
    else:
        # Assert that replay container is empty if no replay files exist in the folder.
        assert not replay_container


def test_unit_death_data_extraction(setup_sc2_major_battles_extractor):
    """
    Test the extraction of unit death data.

    Ensures that the extract method includes unit death data in the replay data.
    - The replay data should contain a 'unit_deaths' key.
    - The value associated with 'unit_deaths' should be a list or another appropriate data structure.
    """
    # Extract data from replays using the SC2MajorBattlesExtractor.
    replay_container = setup_sc2_major_battles_extractor.extract()

    # Verify that the unit death data is correctly populated in the replay data.
    assert replay_container  # Assuming the replay_container is a dictionary and checking if it's not empty.


def test_batch_insert_unit_death_data(setup_sc2_major_battles_extractor):
    """
    Test the insertion of unit death data into the database.

    Verifies that the extracted unit death data is correctly inserted into the database.
    - The test checks that the database contains the expected number of unit death records after insertion.
    - Adjust the assertions based on your database schema and expected outcomes.
    """
    SC2MajorBattleDB.init(
        "test_sc2_major_battle_extractor_db"
    )  # Initialize the test database.

    data_storage = (
        UnitDeathDataStorage()
    )  # Create an instance of UnitDeathDataStorage to hold unit death data.

    # Define sample unit death records for testing.
    unit_death_one = (1, 100, 325)
    unit_death_two = (2, 150, 175)
    unit_death_three = (3, 180, 200)

    # Add unit death data to the storage.
    data_storage.set_data(unit_death_one)
    data_storage.set_data(unit_death_two)
    data_storage.set_data(unit_death_three)

    # Insert the unit death data into the database using the extractor's batch insert method.
    setup_sc2_major_battles_extractor._batch_insert([data_storage])

    # Verify that the first record in the database matches the first unit death record.
    assert SC2MajorBattleDB.get_unit_deaths()[0] == unit_death_one

    # Clean up: Delete all records from the UnitDeath table and dispose of the database connection.
    with SC2MajorBattleDB.Session() as session:
        session.query(UnitDeath).delete()
        session.commit()
    SC2MajorBattleDB.engine.dispose()

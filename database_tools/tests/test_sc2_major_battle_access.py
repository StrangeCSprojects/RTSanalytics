import pytest
from unittest.mock import patch
from database_tools.general.general_database_access import DataStorage
from database_tools.sc2.sc2_major_battle_database import SC2MajorBattleDB
from database_tools.sc2.sc2_major_battle_access import UnitDeathDataStorage


@pytest.fixture
def unit_death_data_storage():
    """
    Pytest fixture to create an instance of UnitDeathDataStorage for use in tests.
    """
    data_storage = UnitDeathDataStorage()
    data_storage._data = []
    return data_storage


def test_set_data(unit_death_data_storage):
    """
    Test the set_data method to ensure it correctly appends new records.
    """
    new_record = (1, 100, 50)
    unit_death_data_storage.set_data(new_record)

    # Verify that the data was appended to the internal list
    assert len(unit_death_data_storage._data) == 1
    assert unit_death_data_storage._data[0] == new_record


@patch.object(SC2MajorBattleDB, 'add_unit_deaths', return_value=None)
def test_push(mock_add_unit_deaths, unit_death_data_storage):
    """
    Test the push method to ensure it calls SC2MajorBattleDB.add_unit_deaths correctly.
    """
    # Add some test data
    unit_death_data_storage._data = [(1, 100, 50), (2, 200, 30)]

    # Call the push method
    unit_death_data_storage.push()

    # Verify that the add_unit_deaths method was called with the correct data
    mock_add_unit_deaths.assert_called_once_with(unit_death_data_storage._data)


def test_push_no_data(unit_death_data_storage):
    """
    Test the push method when there is no data to ensure it handles this case gracefully.
    """
    # Ensure data is empty
    unit_death_data_storage._data = []

    with patch.object(SC2MajorBattleDB, 'add_unit_deaths') as mock_add_unit_deaths:
        unit_death_data_storage.push()

        # Verify that add_unit_deaths was not called since there was no data
        mock_add_unit_deaths.assert_not_called()

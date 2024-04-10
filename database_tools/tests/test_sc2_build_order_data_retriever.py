from platform import java_ver
import pytest
from unittest.mock import Mock
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB
from database_tools.sc2.sc2_build_order_data_retriever import SC2BuildOrderDataRetriever


@pytest.fixture(scope="module")
def setup_database():
    # Set up the database
    SC2BuildOrderDB.init("test_build_orders")
    data_retriever = SC2BuildOrderDataRetriever(SC2BuildOrderDB)
    yield data_retriever # Yields the database instance


def test_get_build_by_name(setup_database):
    test_name = "test build"
    test_build = setup_database.get_build_by_name(test_name)
    assert not test_build # This build does not exist
    
    # Add the build and try again
    test_build = "test1", "race1", '[[[[unit type, unit name], 10], 1]]'
    SC2BuildOrderDB.add_build_orders([test_build])
    test_build = setup_database.get_build_by_name(test_name)
    assert test_build[0] == "test1"
    assert test_build[1] == "race1"
    assert test_build[2] == [((("unit type", "unit name"), 10), 1)]

def test_get_builds_by_race():
    # Test the get builds by race function

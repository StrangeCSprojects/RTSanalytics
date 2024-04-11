import pytest
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB
from database_tools.sc2.sc2_build_order_data_retriever import SC2BuildOrderDataRetriever


@pytest.fixture(scope="module")
def setup_database():
    # Set up the database
    SC2BuildOrderDB.init("test_build_db")
    data_retriever = SC2BuildOrderDataRetriever(SC2BuildOrderDB)
    yield data_retriever # Yields the database instance


def test_get_build_by_name(setup_database):
    test_name = "test build"
    test_build_one = setup_database.get_build_by_name(test_name)
    assert not test_build_one # This build does not exist
    
    # Add the build and try again
    test_build_two = ("test1", "race1", '[[[["unit_type", "unit_name"], 10], 1]]')
    SC2BuildOrderDB.add_build_orders([test_build_two])
    test_build_three = setup_database.get_build_by_name("test1")
    # print(test_build_three)
    assert test_build_three[0] == "race1"
    assert test_build_three[1] == [((("unit_type", "unit_name"), 10), 1)]

def test_get_builds_by_race(setup_database):
    # Test the get builds by race function
    test_build_one = ("test1", "race1", '[[[["unit_type", "unit_name"], 10], 1]]')
    test_build_two = ("test2", "race1", '[[[["unit_type", "unit_name"], 10], 1]]')
    test_build_three = ("test3", "race2", '[[[["unit_type", "unit_name"], 10], 1]]')

    test_builds = [test_build_one,test_build_two,test_build_three]

    SC2BuildOrderDB.add_build_orders(test_builds)

    test_race_builds = setup_database.get_all_builds_by_race("race1")

    assert len(test_race_builds) == 2
    assert test_race_builds[0][0] == "test1"
    assert test_race_builds[1][0] == "test2"

    assert test_race_builds[0][1] == [((("unit_type", "unit_name"), 10), 1)]
    assert test_race_builds[1][1] == [((("unit_type", "unit_name"), 10), 1)]


import pytest
from sqlalchemy.orm import declarative_base
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB
from database_tools.sc2.entities.sc2_build_order_entities import PlayerBuildOrder


Base = declarative_base()  # Define Base using declarative_base() from sqlalchemy.orm


# Fixture to set up and tear down the database connection for each test
@pytest.fixture()
def setup_database(scope="module"):
    # Initialize the test database
    SC2BuildOrderDB.init("test_build_db")
    yield  # Run the tests
    # Clean the data from relevant tables after all tests are finished
    with SC2BuildOrderDB.Session() as session:
        session.query(PlayerBuildOrder).delete()
        session.commit()
    # Close the database connection after cleaning
    SC2BuildOrderDB.engine.dispose()


# Test cases
def test_add_build_orders(setup_database):
    # Create a list of play data
    builds = [
        ("build1", "race1", '[["command list 1"], ["command list 2"]]'),
        ("build2", "race2", '[["command list 3"], ["command list 4"]]')
    ]
    
    # Add the build data to the database
    SC2BuildOrderDB.add_build_orders(builds)
    
    # Retrieve all builds from the database
    all_builds = SC2BuildOrderDB.get_builds()
    
    # Check if the builds were added correctly
    assert all_builds = tuple(builds)

    # Attempt to add the same builds again
    SC2BuildOrderDB.add_build_orders(builds)
    
    # Check that the duplicate builds weren't added
    with SC2BuildOrderDB.Session() as session:
        num_builds_in_db = session.query(PlayerBuildOrder).count()
        assert num_builds_in_db == 2


def test_get_build_by_name(setup_database):
    # Attempt to get a build that doesn't exist
    new_build = SC2BuildOrderDB.get_build_by_name("new build")
    assert not new_build # fake_build is equal to None
    
    # Add the new build to the database
    new_build = ("new build", "new race", '[["new commands 1"], ["new commands 2"]]')
    SC2BuildOrderDB.add_build_orders([new_build])
    
    # Now try retrieving the new build
    new_build = SC2BuildOrderDB.get_build_by_name("new build")
    
    assert new_build # new_build should no longer be equal to None


def test_get_builds(setup_database):
    # Get all the builds in the build order database
    all_builds = SC2BuildOrderDB.get_builds()
    
    # Check for correct number of builds and names
    assert len(all_builds) == 3 # All the builds added to test database file
    for build in all_builds:
        assert SC2BuildOrderDB.get_build_by_name(build[0])

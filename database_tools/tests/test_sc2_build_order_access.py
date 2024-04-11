import pytest
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB
from database_tools.sc2.entities.sc2_build_order_entities import PlayerBuildOrder
from database_tools.sc2.sc2_build_order_access import BuildOrderDataStorage


# Fixture to set up and tear down the database connection for each test
@pytest.fixture(scope="module")
def setup_database():
    # Initialize the test database
    SC2BuildOrderDB.init("test_build_db")
    yield  # Run the tests
    # Clean the data from relevant tables after all tests are finished
    with SC2BuildOrderDB.Session() as session:
        session.query(PlayerBuildOrder).delete()
        session.commit()
    # Close the database connection after cleaning
    SC2BuildOrderDB.engine.dispose()


def test_push_build_data(setup_database):
    # Initialize data storage
    build_storage = BuildOrderDataStorage()
    build_data = ("name1", "race1", [["command list 1"], ["command list 2"]])
    build_storage.set_data(build_data)

    # Push the data to the database
    build_storage.push()

    # Check if the data was added to the database
    with SC2BuildOrderDB.Session() as session:
        build = session.query(PlayerBuildOrder).filter_by(name="name1").first()
        assert build is not None
        assert build.race == "race1"
        assert build.commands == '[["command  list 1], ["command list 2"]]'

    # Attempt to push the same game data again
    build_storage.push()

    # Check if the build data was added only once
    with SC2BuildOrderDB.Session() as session:
        num_builds = session.query(PlayerBuildOrder).filter_by(name="name1").count()

    assert num_builds == 1

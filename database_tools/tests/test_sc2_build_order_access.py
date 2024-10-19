import pytest
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB
from database_tools.sc2.entities.sc2_build_order_entities import BuildTemplate
from database_tools.sc2.sc2_build_order_access import BuildOrderDataStorage


# Fixture to set up and tear down the database connection for each test
@pytest.fixture(scope="module")
def setup_database():
    # Initialize the test database
    SC2BuildOrderDB.init("test_build_db")
    yield  # Run the tests
    # Clean the data from relevant tables after all tests are finished
    with SC2BuildOrderDB.Session() as session:
        session.query(BuildTemplate).delete()
        session.commit()
    # Close the database connection after cleaning
    SC2BuildOrderDB.engine.dispose()


def test_push_build_data(setup_database):
    # Initialize data storage
    build_storage = BuildOrderDataStorage()
    build_data = ("name1", "race1", [((("unit_name_one", "unit_type_one"),10),1), ((("unit_name_two", "unit_type_two"),15),1)])
    build_storage.set_data(build_data)

    # Push the data to the database
    build_storage.push()

    # Check if the data was added to the database
    with SC2BuildOrderDB.Session() as session:
        build = session.query(BuildTemplate).filter_by(name="name1").first()
        assert build is not None
        assert build.race == "race1"
        # print(build.commands)
        assert build.commands == '[[[["unit_name_one", "unit_type_one"], 10], 1], [[["unit_name_two", "unit_type_two"], 15], 1]]'

    # Attempt to push the same game data again
    build_storage.push()

    # Check if the build data was added only once
    with SC2BuildOrderDB.Session() as session:
        num_builds = session.query(BuildTemplate).filter_by(name="name1").count()

    assert num_builds == 1

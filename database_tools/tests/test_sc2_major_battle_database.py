import pytest
from sqlalchemy import (
    create_engine,
)  # Import create_engine for creating a new SQLAlchemy engine instance.
from sqlalchemy.orm import (
    sessionmaker,
)  # Import sessionmaker for managing sessions with the database.
from unittest.mock import patch  # Import patch for mocking in unit tests.
from database_tools.sc2.entities.sc2_major_battle_entities import (
    UnitDeath,
    Base,
)  # Import ORM entities and Base for schema.
from database_tools.sc2.sc2_major_battle_database import (
    SC2MajorBattleDB,
)  # Import SC2MajorBattleDB for database operations.


@pytest.fixture(scope="module")
def setup_database():
    """
    Fixture to set up an in-memory database and initialize the SC2MajorBattleDB class.
    This fixture is scoped to the module, meaning it will be run once per test module.
    """
    # Use an in-memory SQLite database for testing, which exists only in memory and is discarded after use.
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)  # Create all tables in the database schema.
    SC2MajorBattleDB.Session = sessionmaker(
        bind=engine
    )  # Bind a new sessionmaker to the in-memory engine.
    yield
    # Teardown: Clean up data from relevant tables after all tests are finished.
    with SC2MajorBattleDB.Session() as session:
        session.query(
            UnitDeath
        ).delete()  # Delete all records from the UnitDeath table.
        session.commit()
    # Dispose of the engine to close the database connection.
    SC2MajorBattleDB.engine.dispose()


@pytest.fixture()
def session():
    """
    Fixture to create a new session for each test.
    This ensures that each test has a clean session to work with, which is closed after the test completes.
    """
    session = SC2MajorBattleDB.Session()  # Start a new session.
    yield session
    session.close()  # Close the session after the test is done.


def test_init(setup_database):
    """
    Test initializing the database connection.
    Ensures that the SC2MajorBattleDB initializes the engine and sessionmaker correctly.
    """
    SC2MajorBattleDB.init("test_sc2_major_battle_db")
    assert SC2MajorBattleDB.engine is not None  # Check that the engine is initialized.
    assert (
        SC2MajorBattleDB.Session is not None
    )  # Check that the sessionmaker is initialized.


def test_add_unit_deaths(setup_database, session):
    """
    Test adding multiple unit deaths to the database.
    Verifies that unit deaths are correctly added to the database and that the records match the input data.
    """
    unit_deaths = [(1, 100, 50), (2, 200, 75)]
    SC2MajorBattleDB.add_unit_deaths(
        unit_deaths
    )  # Add multiple unit deaths to the database.
    result = session.query(UnitDeath).all()  # Query all unit deaths from the database.
    assert len(result) == 2  # Check that two records were added.
    assert result[0].id == 1  # Validate the ID of the first unit death.
    assert result[0].time == 100  # Validate the time of the first unit death.
    assert (
        result[0].resource == 50
    )  # Validate the resource value of the first unit death.
    assert result[1].id == 2  # Validate the ID of the second unit death.
    assert result[1].time == 200  # Validate the time of the second unit death.
    assert (
        result[1].resource == 75
    )  # Validate the resource value of the second unit death.

    # Cleanup: Delete all records from the UnitDeath table to reset the database state.
    with SC2MajorBattleDB.Session() as session:
        session.query(UnitDeath).delete()
        session.commit()


def test_get_unit_death_by_id(setup_database, session):
    """
    Test retrieving a unit death by its ID.
    Ensures that a specific unit death can be retrieved correctly by its ID, and checks for non-existing IDs.
    """
    unit_deaths = [(3, 300, 100)]
    SC2MajorBattleDB.add_unit_deaths(unit_deaths)  # Add a unit death to the database.
    result = SC2MajorBattleDB.get_unit_death_by_id(3)  # Retrieve the unit death by ID.
    assert result == (
        3,
        300,
        100,
    )  # Check that the retrieved data matches the input data.

    # Test retrieving a non-existing unit death.
    result = SC2MajorBattleDB.get_unit_death_by_id(
        99
    )  # Attempt to retrieve a non-existing unit death.
    assert result is None  # Check that the result is None when the ID does not exist.

    # Cleanup: Delete all records from the UnitDeath table to reset the database state.
    with SC2MajorBattleDB.Session() as session:
        session.query(UnitDeath).delete()
        session.commit()


def test_get_unit_deaths(setup_database, session):
    """
    Test retrieving all unit deaths from the database.
    Verifies that all unit deaths can be retrieved correctly and that the data matches the input.
    """
    unit_deaths = [(4, 400, 150), (5, 500, 200)]
    SC2MajorBattleDB.add_unit_deaths(
        unit_deaths
    )  # Add multiple unit deaths to the database.
    result = SC2MajorBattleDB.get_unit_deaths()  # Retrieve all unit deaths.
    assert len(result) == 2  # Check that two records are retrieved.
    assert result == (
        (4, 400, 150),
        (5, 500, 200),
    )  # Validate that the retrieved data matches the input data.

    # Cleanup: Delete all records from the UnitDeath table to reset the database state.
    with SC2MajorBattleDB.Session() as session:
        session.query(UnitDeath).delete()
        session.commit()


def test_log_name_not_found(setup_database):
    """
    Test logging when a unit death ID is not found.
    Ensures that the appropriate warning message is logged when attempting to retrieve a non-existing unit death ID.
    """
    # Use patch to mock the logging.warning function and check if it gets called with the correct message.
    with patch("logging.warning") as mock_warning:
        SC2MajorBattleDB._log_name_not_found(
            42
        )  # Attempt to log a warning for a non-existing unit death ID.
        mock_warning.assert_called_once_with(
            "Unit: 42 - Unit not found. - Ignore if adding unit to database"
        )  # Verify the warning message.

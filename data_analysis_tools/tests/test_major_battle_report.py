import pytest
from data_analysis_tools.general.reports.major_battle_timestamps import (
    MajorBattleReport,
)  # Import MajorBattleReport for generating reports on major battles.
from database_tools.sc2.sc2_major_battle_retriever import (
    SC2MajorBattleDataRetriever,
)  # Import DataRetriever for retrieving unit death data from the database.
from database_tools.sc2.sc2_major_battle_database import (
    SC2MajorBattleDB,
)  # Import SC2MajorBattleDB for database operations.
from database_tools.sc2.entities.sc2_major_battle_entities import (
    UnitDeath,
)  # Import UnitDeath entity for database interactions.


@pytest.fixture(scope="module")
def setup_database():
    """
    Fixture to create and initialize a test database for the SC2MajorBattleDB class.
    Sets up the database before tests and tears down after all tests are done.
    """
    SC2MajorBattleDB.init(
        "test_sc2_major_battle_report"
    )  # Initialize the test database.
    yield SC2MajorBattleDB  # Provide the initialized database to tests.
    clear_database()  # Clean up the database after all tests are finished.


@pytest.fixture
def data_retriever(setup_database):
    """
    Fixture to provide an instance of SC2MajorBattleDataRetriever with a test database.
    Ensures the retriever is configured with the test database for consistent test results.
    """
    return SC2MajorBattleDataRetriever(
        setup_database
    )  # Use the initialized test database for data retrieval.


@pytest.fixture
def major_battle_report(data_retriever):
    """
    Fixture to create an instance of MajorBattleReport using a test DataRetriever.
    Provides the MajorBattleReport instance configured with the test data retriever.
    """
    return MajorBattleReport(data_retriever=data_retriever)


def test_configure_report_no_deaths(major_battle_report):
    """
    Test configure_report method with no unit deaths in the database.
    Ensures the report correctly identifies no major battles when there are no unit deaths.
    """
    result = (
        major_battle_report.configure_report()
    )  # Generate report with no unit deaths.

    assert result == []  # Expect no major battles.
    clear_database()  # Clear database after the test.


def test_configure_report_deaths_below_threshold(major_battle_report, setup_database):
    """
    Test configure_report method with unit deaths below the resource threshold.
    Ensures that no major battles are reported when all unit deaths have resource values below the threshold.
    """
    # Insert unit deaths with total resource value below the threshold.
    setup_database.add_unit_deaths(
        [
            (1, 10, 1000),  # (unit_name, time_of_death, resource_value)
            (2, 12, 1000),
            (3, 14, 1000),
        ]
    )

    result = major_battle_report.configure_report()  # Generate report.

    assert result == []  # Expect no major battles.
    clear_database()  # Clear database after the test.


def test_configure_report_deaths_just_meeting_threshold(
    major_battle_report, setup_database
):
    """
    Test configure_report method with unit deaths that just meet the resource threshold.
    Verifies that a major battle is reported when unit deaths meet the exact resource threshold within the detection window.
    """
    # Insert unit deaths with total resource value just meeting the threshold.
    setup_database.add_unit_deaths([(1, 10, 2000), (2, 12, 2000), (3, 14, 1000)])

    result = major_battle_report.configure_report()  # Generate report.

    assert result == [(10, 14)]  # Expect one major battle.
    clear_database()  # Clear database after the test.


def test_configure_report_deaths_exceeding_threshold_within_detection_window(
    major_battle_report, setup_database
):
    """
    Test configure_report method with unit deaths that exceed the threshold within the detection window.
    Verifies that a major battle is correctly identified when unit deaths exceed the resource threshold within the detection window.
    """
    # Insert unit deaths with resource values exceeding the threshold within the detection window.
    setup_database.add_unit_deaths(
        [
            (1, 10, 2000),
            (2, 20, 3000),  # Within the detection window.
            (3, 40, 4000),  # Exceeds detection window.
        ]
    )

    result = major_battle_report.configure_report()  # Generate report.

    assert result == [(10, 20)]  # Expect one major battle within the detection window.
    clear_database()  # Clear database after the test.


def test_configure_report_deaths_multiple_battles(major_battle_report, setup_database):
    """
    Test configure_report method with multiple sets of deaths forming separate battles.
    Verifies that multiple major battles are correctly identified when they occur within different detection windows.
    """
    # Insert unit deaths for multiple major battles.
    setup_database.add_unit_deaths(
        [
            (1, 10, 2000),
            (2, 12, 3000),  # First major battle ends here.
            (3, 50, 2000),
            (4, 52, 3000),  # Second major battle ends here.
        ]
    )

    result = major_battle_report.configure_report()  # Generate report.

    assert result == [(10, 12), (50, 52)]  # Expect two separate major battles.
    clear_database()  # Clear database after the test.


def test_configure_report_deaths_spanning_detection_window(
    major_battle_report, setup_database
):
    """
    Test configure_report method with deaths that span the detection window.
    Ensures that only deaths within the detection window contribute to the same battle.
    """
    # Insert unit deaths where only some are within the same detection window.
    setup_database.add_unit_deaths(
        [(1, 10, 2000), (2, 30, 2000), (3, 32, 1000)]  # Outside the detection window.
    )

    result = major_battle_report.configure_report()  # Generate report.

    assert (
        result == []
    )  # Expect no major battles as resource values do not sum up within the detection window.
    clear_database()  # Clear database after the test.


def clear_database():
    """
    Helper function to clear all data from the UnitDeath table in the test database.
    Ensures the database is reset after each test to maintain isolation and prevent cross-test interference.
    """
    with SC2MajorBattleDB.Session() as session:
        session.query(
            UnitDeath
        ).delete()  # Delete all records from the UnitDeath table.
        session.commit()
    SC2MajorBattleDB.engine.dispose()  # Dispose of the engine to close the database connection.

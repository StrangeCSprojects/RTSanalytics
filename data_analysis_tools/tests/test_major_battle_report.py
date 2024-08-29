import pytest
from data_analysis_tools.general.reports.major_battle_report import MajorBattleReport
from database_tools.general.data_retriever import DataRetriever
from database_tools.general.general_database import GeneralDB


@pytest.fixture(scope="module")
def setup_database():
    """Creates a database file to be used for testing"""
    # Initialize the test database
    GeneralDB.init("test_analyzer_db")
    yield  # Run the tests
    GeneralDB.engine.dispose()

@pytest.fixture
def data_retriever(setup_database):
    """Fixture to provide an instance of DataRetriever with a test database."""
    # Use the initialized test database for data retrieval
    return DataRetriever()

@pytest.fixture
def major_battle_report(data_retriever):
    """Fixture to create an instance of MajorBattleReport using a test DataRetriever."""
    return MajorBattleReport(data_retriever=data_retriever)

def test_configure_report_no_deaths(major_battle_report):
    """Test configure_report with no unit deaths."""
    # Assume the database setup has no unit death entries for this test
    result = major_battle_report.configure_report()

    # Expect no major battles
    assert result == []

def test_configure_report_deaths_below_threshold(major_battle_report, setup_database):
    """Test configure_report with unit deaths below the resource threshold."""
    # Setup database to return a list of unit deaths below the threshold
    # This step involves inserting mock data into the database
    setup_database.insert_unit_deaths([
        ('Unit1', 10, 1000),  # (unit_name, time_of_death, resource_value)
        ('Unit2', 12, 1000),
        ('Unit3', 14, 1000)
    ])

    result = major_battle_report.configure_report()

    # Expect no major battles
    assert result == []

def test_configure_report_deaths_just_meeting_threshold(major_battle_report, setup_database):
    """Test configure_report with unit deaths that just meet the resource threshold."""
    # Insert mock data into the database that meets the threshold
    setup_database.insert_unit_deaths([
        ('Unit1', 10, 2000),
        ('Unit2', 12, 2000),
        ('Unit3', 14, 1000)
    ])

    result = major_battle_report.configure_report()

    # Expect one major battle
    assert result == [(10, 14)]

def test_configure_report_deaths_exceeding_threshold_within_detection_window(major_battle_report, setup_database):
    """Test configure_report with unit deaths that exceed the threshold within the detection window."""
    # Insert mock data into the database that exceeds the threshold within the detection window
    setup_database.insert_unit_deaths([
        ('Unit1', 10, 2000),
        ('Unit2', 20, 3000),  # Within the detection window
        ('Unit3', 40, 4000)   # Exceeds detection window
    ])

    result = major_battle_report.configure_report()

    # Expect one major battle for the first two deaths and ignore the last one due to exceeding detection window
    assert result == [(10, 20)]

def test_configure_report_deaths_multiple_battles(major_battle_report, setup_database):
    """Test configure_report with multiple sets of deaths forming separate battles."""
    # Insert mock data into the database for multiple major battles
    setup_database.insert_unit_deaths([
        ('Unit1', 10, 2000),
        ('Unit2', 12, 3000),  # First major battle ends here
        ('Unit3', 50, 2000),
        ('Unit4', 52, 3000)   # Second major battle ends here
    ])

    result = major_battle_report.configure_report()

    # Expect two separate major battles
    assert result == [(10, 12), (50, 52)]

def test_configure_report_deaths_spanning_detection_window(major_battle_report, setup_database):
    """Test configure_report with deaths that span the detection window."""
    # Insert mock data into the database where only some are in the same battle due to detection window
    setup_database.insert_unit_deaths([
        ('Unit1', 10, 2000),
        ('Unit2', 30, 2000),  # Outside the detection window, should not be counted in the same battle
        ('Unit3', 32, 1000)
    ])

    result = major_battle_report.configure_report()

    # Expect no major battles as the resource values do not sum up within the detection window
    assert result == []

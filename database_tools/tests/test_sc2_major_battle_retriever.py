import pytest
from database_tools.sc2.sc2_major_battle_database import SC2MajorBattleDB
from database_tools.sc2.sc2_major_battle_retriever import SC2MajorBattleDataRetriever
from database_tools.sc2.entities.sc2_major_battle_entities import UnitDeath


@pytest.fixture
def setup_database():
    """Fixture to create a mock database."""
    # Create a mock instance of SC2MajorBattleDB
    SC2MajorBattleDB.init("test_sc2_major_battle_db")
    data_retriever = SC2MajorBattleDataRetriever(SC2MajorBattleDB)
    yield data_retriever
    # Clean the data from relevant tables after all tests are finished
    with SC2MajorBattleDB.Session() as session:
        session.query(UnitDeath).delete()
        session.commit()
    # Close the database connection after cleaning
    SC2MajorBattleDB.engine.dispose()


def test_get_all_unit_deaths(setup_database):
    """Test retrieving all unit deaths from the database."""

    SC2MajorBattleDB.add_unit_deaths(((1, 100, 50), (2, 200, 75)))

    result = setup_database.get_all_unit_deaths()

    # Verify that the method returns the correct unit deaths
    assert result == ((1, 100, 50), (2, 200, 75))

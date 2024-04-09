import pytest
from data_analysis_tools.sc2.sc2_build_order.sc2_determine_build import SC2DetermineBuild
from database_tools.sc2.sc2_build_order_data_retriever import SC2BuildOrderDataRetriever
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB
from math import inf
from json import loads, dumps

@pytest.fixture(scope="module")
def setup_database():
    """Creates a database file to be used for testing"""
    # Initialize the test database
    SC2BuildOrderDB.init("test_sc2_determine_build_db")
    yield  # Run the tests
    SC2BuildOrderDB.engine.dispose()

def test_determine_build(setup_database):
    database = SC2BuildOrderDB
    data_retriever = SC2BuildOrderDataRetriever(database)
    determine_build = SC2DetermineBuild(data_retriever)

    build_one = (("Three CC Battle-Mech","Terran", [
         ((("UnitInitEvent", "SupplyDepot"),10),1),
         ((("UnitInitEvent", "Barracks"),20),1),
         ((("UnitInitEvent", "CommandCenter"),40),1),
         ((("UnitInitEvent", "CommandCenter"),70),1),
         ((("UnitInitEvent", "Factory"),80),1),
         ((("UnitInitEvent", "Starport"),100),1),
         ((("UnitInitEvent", "Factory"),110),1),
         ((("UnitInitEvent", "Factory"),110),1),
         ((("UnitInitEvent", "Armory"),150),1),
         ((("UnitInitEvent", "Armory"),150),1),
    ]))
    build_two = (("1/1/1 Bio","Terran", [
         ((("UnitInitEvent", "SupplyDepot"),10),1),
         ((("UnitInitEvent", "Barracks"),20),1),
         ((("UnitInitEvent", "CommandCenter"),40),1),
         ((("UnitInitEvent", "Factory"),70),1),
         ((("UnitInitEvent", "Starport"),80),1),
         ((("UnitInitEvent", "Barracks"),100),1),
         ((("UnitInitEvent", "Barracks"),110),1),
         ((("UnitInitEvent", "CommandCenter"),130),1),
         ((("UnitInitEvent", "Barracks"),150),1),
         ((("UnitInitEvent", "Barracks"),150),1),
         ((("UnitInitEvent", "EngineBay"),170),1),
         ((("UnitInitEvent", "EngineBay"),170),1),
    ]))
    build_three = (("Threaper Bio", "Terran", [
         ((("UnitInitEvent", "SupplyDepot"),10),1),
         ((("UnitInitEvent", "Barracks"),20),1),
         ((("UnitInitEvent", "Barracks"),22),1),
         ((("UnitInitEvent", "Reaper"),30),1),
         ((("UnitInitEvent", "Reaper"),32),1),
         ((("UnitInitEvent", "Reaper"),35),1),
         ((("UnitInitEvent", "Factory"),50),1),
         ((("UnitInitEvent", "CommandCenter"),70),1),
         ((("UnitInitEvent", "Starport"),100),1),
    ]))
    user_commands = [
         ((("UnitInitEvent", "SupplyDepot"),12),1),
         ((("UnitInitEvent", "Barracks"),22),1),
         ((("UnitInitEvent", "CommandCenter"),50),1),
         ((("UnitInitEvent", "Factory"),90),1),
         ((("UnitInitEvent", "Barracks"),100),1),
         ((("UnitInitEvent", "Barracks"),110),1),
         ((("UnitInitEvent", "Starport"),110),1),
         ((("UnitInitEvent", "Barracks"),150),1),
         ((("UnitInitEvent", "Barracks"),150),1),
         ((("UnitInitEvent", "Barracks"),170),1),
         ((("UnitInitEvent", "EngineBay"),170),1),
         ((("UnitInitEvent", "SupplyDepot"),200),1),
         ((("UnitInitEvent", "Barracks"),250),1),
         ((("UnitInitEvent", "CommandCenter"),275),1),
         ((("UnitInitEvent", "Factory"),300),1),
         ((("UnitInitEvent", "Barracks"),400),1),
         ((("UnitInitEvent", "Barracks"),410),1),
         ((("UnitInitEvent", "Starport"),510),1),
         ((("UnitInitEvent", "Barracks"),750),1),
         ((("UnitInitEvent", "Barracks"),950),1),
         ((("UnitInitEvent", "Barracks"),1070),1),
         ((("UnitInitEvent", "EngineBay"),1070),1),
    ]

    builds_list = [dumps(build_one), dumps(build_two), dumps(build_three)]
    SC2BuildOrderDB.add_build_orders(builds_list)
    race = "Terran"

    assert(determine_build.determine_build(race, user_commands) == "1/1/1 Bio")

def test_compare_build_orders():
    """
    Tests the functionality of comparing user-generated build orders against a benchmark build order in a 
    StarCraft II context. This method assesses how closely a player's build order (timing and sequence of 
    unit and building creation) aligns with an optimal or standard build order.
    """
    # Initialize the mock database and related objects for testing.
    database = SC2BuildOrderDB
    data_retriever = SC2BuildOrderDataRetriever(database)
    determine_build = SC2DetermineBuild(data_retriever)

    # Define the benchmark build order as a sequence of precisely timed commands for unit and building creation.
    benchmark_commands = [
        ((("UnitBornEvent", "SCV"),1),1),
        ((("UnitBornEvent", "SCV"),5),1),
        ((("UnitBornEvent", "SCV"),6),1),
        ((("UnitInitEvent", "Barracks"),10),1),
        ((("UnitInitEvent", "Barracks"),30),1),
        ((("UnitInitEvent", "Barracks"),35),1),
        ((("UnitInitEvent", "Starport"),60),1),
        ((("UnitInitEvent", "CommandCenter"),120),1),
        ((("UnitInitEvent", "Barracks"),120),1),
        ((("UnitInitEvent", "Barracks"),150),1),
        ((("UnitInitEvent", "CommandCenter"),360),1),
    ]

    # Define the user's build order, potentially deviating from the benchmark in timing and sequence.
    user_commands = [
        ((("UnitBornEvent", "SCV"),1),1),
        ((("UnitBornEvent", "SCV"),7),1),
        ((("UnitInitEvent", "Barracks"),12),1),
        ((("UnitInitEvent", "Barracks"),35),1),
        ((("UnitInitEvent", "Barracks"),35),1),  # Duplicate entry to test handling of repeated commands.
        ((("UnitInitEvent", "Starport"),75),1),
        ((("UnitInitEvent", "CommandCenter"),100),1),
        ((("UnitInitEvent", "Barracks"),122),1),
        ((("UnitInitEvent", "Barracks"),146),1),
        ((("UnitInitEvent", "CommandCenter"),400),1),
    ]

    # Assert that the calculated discrepancy between the benchmark and user's build orders is as expected.
    assert round(determine_build._compare_build_orders(benchmark_commands, user_commands),2) == .23

def test_relative_error_of_unit_type():
    """
    The test assesses the relative error calculation for multiple unit types.
    The relative error is computed as the average deviation of the user's 
    timings from the benchmark timings, normalized by the benchmark timings to provide a percentage error 
    that is easier to interpret.

    The assertions check that the calculated relative errors for each unit type are within expected bounds, 
    demonstrating the method's ability to accurately reflect discrepancies in build order execution.
    """
    # Initialize the mock database and related objects for testing.
    database = SC2BuildOrderDB
    data_retriever = SC2BuildOrderDataRetriever(database)
    determine_build = SC2DetermineBuild(data_retriever)

    # Define benchmark timings for various units and buildings as they would appear in an ideal build order.
    benchmark_unit_dictionary = {
        ("UnitBornEvent", "SCV"): [1, 5, 6],
        ("UnitInitEvent", "CommandCenter"): [120, 360],
        ("UnitInitEvent", "Barracks"): [10, 30, 35, 120, 150],
        ("UnitInitEvent", "Starport"): [60]
    }
    
    # Define user's timings for the same units and buildings, simulating real gameplay where timings might not be perfect.
    user_unit_dictionary = {
        ("UnitBornEvent", "SCV"): [1, 7, float('inf')],  # Use 'inf' to simulate a missed timing or a significantly delayed event.
        ("UnitInitEvent", "CommandCenter"): [100, 400],
        ("UnitInitEvent", "Barracks"): [12, 35, 35, 122, 146],
        ("UnitInitEvent", "Starport"): [75]
    }
    
    # Unit types to be tested for relative error in their build timings.
    unit_type_one = ("UnitBornEvent", "SCV")
    unit_type_two = ("UnitInitEvent", "CommandCenter")
    unit_type_three = ("UnitInitEvent", "Barracks")
    unit_type_four = ("UnitInitEvent", "Starport")
    
    # Assert the calculated relative errors for each unit type against expected values, rounding to two decimal places for comparison.
    assert round(determine_build._relative_error_of_unit_type(benchmark_unit_dictionary, user_unit_dictionary, unit_type_one), 2) == 0.47
    assert round(determine_build._relative_error_of_unit_type(benchmark_unit_dictionary, user_unit_dictionary, unit_type_two), 2) == 0.14
    assert round(determine_build._relative_error_of_unit_type(benchmark_unit_dictionary, user_unit_dictionary, unit_type_three), 2) == 0.08
    assert round(determine_build._relative_error_of_unit_type(benchmark_unit_dictionary, user_unit_dictionary, unit_type_four), 2) == 0.25

def test_load_unit_dictionary():
    """
    This method populates a dictionary with unit types and their initialization times, handling both new entries
    and updates to existing ones. The test sequentially adds units to the dictionary and asserts the correctness
    of the dictionary's state after each addition.
    """
    # Initialize the mock database and related objects for testing.
    database = SC2BuildOrderDB
    data_retriever = SC2BuildOrderDataRetriever(database)
    determine_build = SC2DetermineBuild(data_retriever)

    # Initialize an empty dictionary for tracking units and their initialization times.
    unit_dictionary = {}

    # Add the first unit type (Barracks) and its initialization time, then assert the dictionary state.
    unit_type_one = ("UnitInitEvent", "Barracks")
    time_one = 5
    determine_build._load_unit_dictionary(unit_dictionary, unit_type_one, time_one)
    assert unit_dictionary == {("UnitInitEvent", "Barracks"): [5]}

    # Add a different unit type (SupplyDepot) and its time, then assert the updated dictionary state.
    unit_type_two = ("UnitInitEvent", "SupplyDepot")
    time_two = 7
    determine_build._load_unit_dictionary(unit_dictionary, unit_type_two, time_two)
    assert unit_dictionary == {("UnitInitEvent", "Barracks"): [5], ("UnitInitEvent", "SupplyDepot"): [7]}

    # Add the same unit type (Barracks) with a different time, checking for list appending in the dictionary.
    unit_type_three = ("UnitInitEvent", "Barracks")
    time_three = 10
    determine_build._load_unit_dictionary(unit_dictionary, unit_type_three, time_three)
    assert unit_dictionary == {("UnitInitEvent", "Barracks"): [5, 10], ("UnitInitEvent", "SupplyDepot"): [7]}

    # Add a unit with a new event type (UnitBornEvent) to ensure different events create distinct keys.
    unit_type_four = ("UnitBornEvent", "SCV")
    time_four = 15
    determine_build._load_unit_dictionary(unit_dictionary, unit_type_four, time_four)
    assert unit_dictionary == {("UnitInitEvent", "Barracks"): [5, 10], ("UnitInitEvent", "SupplyDepot"): [7], ("UnitBornEvent", "SCV"): [15]}

    # Add the same unit and time (SCV, 15) to test handling of duplicate times within the same unit and event type.
    unit_type_five = ("UnitBornEvent", "SCV")
    time_five = 15
    determine_build._load_unit_dictionary(unit_dictionary, unit_type_five, time_five)
    assert unit_dictionary == {("UnitInitEvent", "Barracks"): [5, 10], ("UnitInitEvent", "SupplyDepot"): [7], ("UnitBornEvent", "SCV"): [15, 15]}

def test_pad_user_unit_dictionary():
    """
    This test simulates the scenario where a user's recorded timestamps for a specific unit type, 
    in this case, "Barracks", are incomplete compared to a benchmark dataset. The benchmark dataset 
    represents an ideal or comprehensive list of timestamps when the "Barracks" unit was initiated 
    during a game.

    The purpose of this test is to ensure that the _pad_user_unit_dictionary method accurately 
    pads the user's dataset with infinite values for missing timestamps, making the user's dataset 
    have the same length as the benchmark.
    """
    benchmark_unit_dictionary = {("UnitInitEvent", "Barracks"): [20,180,181,185,300,301,302,303]}
    user_unit_dictionary = {("UnitInitEvent", "Barracks"): [22,180,181,300,301,303]}
    unit_type = ("UnitInitEvent", "Barracks")

    # Expected outcome after padding the user dictionary to match the benchmark
    padded_dictionary = {("UnitInitEvent", "Barracks"): [22,180,181,300,301,303,float('inf'),float('inf')]}

    # Setup for SC2 build order analysis tools
    database = SC2BuildOrderDB
    data_retriever = SC2BuildOrderDataRetriever(database)
    determine_build = SC2DetermineBuild(data_retriever)

    # Execute the padding method to adjust the user's dictionary
    determine_build._pad_user_unit_dictionary(benchmark_unit_dictionary, user_unit_dictionary, unit_type)

    # Verify the user's dictionary has been correctly padded
    assert user_unit_dictionary == padded_dictionary


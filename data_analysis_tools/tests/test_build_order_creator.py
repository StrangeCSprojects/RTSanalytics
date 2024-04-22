
# Import any needed modules
import os
import pytest
from unittest.mock import patch
from data_analysis_tools.sc2.sc2_build_order.sc2_build_order_creator import SC2BuildOrderCreator

@pytest.fixture
def build_order_creator():
    return SC2BuildOrderCreator()

def test_create_build(build_order_creator):
    build_order_creator.create_build("Test Build", "Protoss", "test_build.csv")
    # Add assertions to check if the build was created successfully
    # For example:
    assert build_order_creator._build_data.get_data() is not None

def test_check_file_type(build_order_creator):
    # Test passes if specified exception type is thrown in the block
    with pytest.raises(ValueError):
        build_order_creator._check_file_type("invalid_file.txt")

def test_check_file_opens(build_order_creator):
    # Test passes if specified exception type is thrown in the block
    with pytest.raises(FileNotFoundError):
        build_order_creator._check_file_opens("nonexistent_file.csv")

def test_check_command_length(build_order_creator):
    # Test passes if specified exception type is thrown in the block
    with pytest.raises(ValueError):
        build_order_creator._check_command_length("Test Build", ["Probe", "Probe", "20"])

def test_check_headers(build_order_creator):
    # Test passes if specified exception type is thrown in the block
    with pytest.raises(ValueError):
        build_order_creator._check_headers(["Unit_Type", "Unit_Name", "Time (seconds)"])

def test_check_command_time(build_order_creator):
    # Test passes if specified exception type is thrown in the block
    with pytest.raises(ValueError):
        build_order_creator._check_command_time("Probe,Probe,20,0.5", "20", "Probe,Probe,15,0.5", "15", "Test Build")

def test_check_command_weight(build_order_creator):
    # Test passes if specified exception type is thrown in the block
    with pytest.raises(ValueError):
        build_order_creator._check_command_weight("Test Build", ["Probe", "Probe", "20", "1.5"], "1.5")

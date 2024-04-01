"""
    This is a python script used for easier
    debugging of the SC2_RTS_Analytics package
"""

# Import any needed modules
from data_analysis_tools.sc2.sc2_data_retriever import SC2DataRetriever
from replay_extraction_tools.sc2.sc2_extractor import SC2Extractor
from database_tools.sc2.sc2_database import SC2_DB


def main():
    """
    Main entry point
    """
    # Create an extractor and then run it on the replays folder
    extractor = SC2Extractor()
    extractor.run("replay_extraction_tools/replays")

    print("\nImplementing extractor tests...\n")


# Interpret this module
if __name__ == "__main__":
    # Initialize the database
    SC2_DB.init("example_sc2_database")
    main()
    # SC2_DB.engine.dispose()

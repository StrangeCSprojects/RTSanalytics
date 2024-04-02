"""
    This is a python script used for easier
    debugging of the SC2_RTS_Analytics package
"""

# Import any needed modules
from data_analysis_tools.sc2.sc2_data_retriever import SC2DataRetriever
from replay_extraction_tools.sc2.sc2_extractor import SC2Extractor
from database_tools.sc2.sc2_database import SC2_Replay_DB


def main():
    """
    Main entry point
    """
    # Print a hello message to developers!

    print("\nHello there!\n")


# Interpret this module
if __name__ == "__main__":
    # Initialize the database
    SC2_Replay_DB.init("example_sc2_database")
    main()
    # SC2_DB.engine.dispose()

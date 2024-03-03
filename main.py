"""
    This is a python script used for easier
    debugging of the SC2_RTS_Analytics package
"""

# Import any needed modules
from database_tools.sc2_database import SC2_DB
from replay_extraction_tools.sc2_extractor import SC2Extractor


def main():
    """Main entry point"""

    # Create an extractor and then run it on the replays folder
    extractor = SC2Extractor("replay_extraction_tools/replays")
    extractor.run()

    print("SC2 REPLAY DATA HAS BEEN PROCESSED AND STORED!!!\n")


# Interpret this module
if __name__ == "__main__":
    # Initialize the database
    SC2_DB.init("example_sc2_database")
    main()

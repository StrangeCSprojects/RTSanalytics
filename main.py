"""
    This is a python script used for easier
    debugging of the SC2_RTS_Analytics package
"""

# Import any needed modules
from database_tools.sc2_database import SC2_DB
from replay_extraction_tools.sc2_extractor import SC2Extractor


def main():
    """Main entry point"""

    # Initialize the database
    SC2_DB.init("example_sc2_database")
    ext = SC2Extractor("replay_extraction_tools/replays")
    replay_data = ext.extract()
    ext.filter_into_tables(replay_data)
    
    print("\nCOMMANDS ARE NOW ADDED TO TEMPORARY STORAGE!\n")


# Interpret this module
if __name__ == "__main__":
    main()

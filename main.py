
"""
    This is a python script used for easier
    debugging of the SC2_RTS_Analytics package
"""

# Import any needed modules
from database_tools.sc2_database import SC2_DB
from replay_extraction_tools.extractor import *

def main():
    """Main entry point"""
    db = SC2_DB("sc2_games")
    print("It works.")


# Interpret this module
if __name__ == "__main__":
    main()

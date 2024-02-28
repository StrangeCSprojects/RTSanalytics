
"""
    This is a python script used for easier
    debugging of the SC2_RTS_Analytics package
"""

# Import any needed modules
from database_tools.sc2_database import *
from replay_extraction_tools.extractor import *

def main():
    """Main entry point"""
    
    # Initialize the database
    db = SC2_DB("sc2_games")
    
    # Get the replay information
    db.get_player_info(3)


# Interpret this module
if __name__ == "__main__":
    main()

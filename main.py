
"""
    This is a python script used for easier
    debugging of the SC2_RTS_Analytics package
"""

# Import any needed modules
from database_tools.sc2_database import SC2_DB
from replay_extraction_tools.sc2_extractor import *

def main():
    """Main entry point"""
    
    # Ensure the database is initialized
    SC2_DB.create_tables()
    
    # Analyze the replays from the replays folder
    replay_folder_path = "replay_extraction_tools/replays"
    replay_analysis("cstrange", replay_folder_path)
    
    # Test retrieving data from the database
    row = SC2_DB.retrieve_table_data('games', 2) # Get the second replay's data
    for data in row:
        print(data)


# Interpret this module
if __name__ == "__main__":
    main()


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
    extractor = SC2Extractor()
    extractor.run("replay_extraction_tools/replays")

    print("All player IDs...")
    print(SC2_DB.get_all_players())
    print("All game IDs...")
    print(SC2_DB.get_all_games())
    print("Player ID and game ID combos for all replays...")
    print(SC2_DB.get_players_in_game(1))
    print(SC2_DB.get_players_in_game(2))
    print(SC2_DB.get_players_in_game(3))

# Interpret this module
if __name__ == "__main__":
    # Initialize the database
    SC2_DB.init("example_sc2_database")
    main()

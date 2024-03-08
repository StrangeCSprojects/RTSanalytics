
"""
    This is a python script used for easier
    debugging of the SC2_RTS_Analytics package
"""

# Import any needed modules
from data_analysis_tools.sc2.sc2_data_retriever import SC2DataRetriever
from database_tools.sc2_database import SC2_DB
from replay_extraction_tools.sc2_extractor import SC2Extractor


def main():
    """Main entry point"""

    # Create an extractor and then run it on the replays folder
    # FIX THIS CODE
    extractor = SC2Extractor()
    # extractor.run("replay_extraction_tools/replays")

    # THIS CODE WORKS AS LONG AS EXAMPLE DATABASE FILE EXISTS
    print("Calling functions directly from database...")
    print(f"Cody's player data: {SC2_DB.get_player_by_id(2)}")
    print(f"All game data: {SC2_DB.get_all_games()}")
    print(f"All player data: {SC2_DB.get_all_players()}")
    print(f"Data for both players in game #3: {SC2_DB.get_players_in_game(3)}\n")
    
    # Try calling the same functions from data retriever object
    retriever = SC2DataRetriever(SC2_DB)
    print("Calling functions from sc2 data retriever...")
    print(f"Cody's player data: NOT CURRENTLY IMPLEMENTED")
    print(f"All game data: {retriever.get_all_games()}")
    print(f"All player data: {retriever.get_all_players()}")
    print(f"Data for both players in game #3: {retriever.get_players_in_game(3)}\n")

# Interpret this module
if __name__ == "__main__":
    # Initialize the database
    SC2_DB.init("example_sc2_database")
    main()

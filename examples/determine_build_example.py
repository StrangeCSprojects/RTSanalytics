from data_analysis_tools.sc2.sc2_build_order.sc2_build_order_creator import SC2BuildOrderCreator
from database_tools.sc2.sc2_RTSA_DB import SC2BuildOrderDB
from data_analysis_tools.sc2.sc2_build_order.sc2_determine_build import SC2DetermineBuild
from database_tools.sc2.sc2_build_order_data_retriever import SC2BuildOrderDataRetriever
from replay_extraction_tools.sc2.sc2_extractor import SC2Extractor
from database_tools.sc2.sc2_replay_database import SC2ReplayDB
from database_tools.sc2.sc2_replay_data_retriever import SC2ReplayDataRetriever
from data_analysis_tools.sc2.sc2_analyzer import SC2Analyzer
from config.sc2_logging_config import setup_logging

def main():
    """
    This example shows how to:
        - Setup logging capabilites
        - Create build orders and add them to database
        - Read in user replays to a database
        - Determine winrates based on race and build
    """
    # Setup logging capabilites
    setup_logging()

    # Initi
    SC2BuildOrderDB.init("build_order")
    SC2ReplayDB.init("replay")

    # sc2_extractor
    sc2_extractor = SC2Extractor()
    sc2_extractor.run("examples/sc2_build_replays")

    # sc2_replay_data_retriever
    replay_data_retriever = SC2ReplayDataRetriever(SC2ReplayDB)

    # sc2_build_order_data_retriever
    build_order_data_retriever = SC2BuildOrderDataRetriever(SC2BuildOrderDB)


    # #sc2_determine_build
    sc2_determine_build = SC2DetermineBuild(build_order_data_retriever)
    commands = replay_data_retriever.get_commands(1,2)
    build = sc2_determine_build.determine_build("Terran", commands)
    print(build)
    
        
    
if __name__ == "__main__":
    main()
from data_analysis_tools.sc2.sc2_build_order.sc2_build_order_creator import SC2BuildOrderCreator
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB
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

    # sc2_build_order_creator
    build_order_creator = SC2BuildOrderCreator()
    build_order_creator.create_build("ThreeRaxBio", "Terran", "three_rax_bio.csv")
    build_order_creator.create_build("TwoBaseBlink", "Protoss", "two_base_blink.csv")

    # sc2_extractor
    sc2_extractor = SC2Extractor()
    sc2_extractor.run("replay_extraction_tools/tests/test_replays")

    # sc2_replay_data_retriever
    replay_data_retriever = SC2ReplayDataRetriever(SC2ReplayDB)

    # sc2_build_order_data_retriever
    build_order_data_retriever = SC2BuildOrderDataRetriever(SC2BuildOrderDB)

    # sc2_analyzer
    sc2_analyzer = SC2Analyzer(replay_data_retriever)
    sc2_analyzer.winrate_build(build_order_data_retriever)
    sc2_analyzer.winrate_race()
        
    
if __name__ == "__main__":
    main()
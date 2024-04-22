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
    build_order_creator.create_build("OneOneOneBio", "Terran", "1-1-1_bio.csv")
    build_order_creator.create_build("CruiserMech", "Terran", "cruiser_mech.csv")
    build_order_creator.create_build("PheonixColossus", "Protoss", "eco_pheonix_colossus.csv")
    build_order_creator.create_build("GreedyLurkers", "Zerg", "greedy_lurkers.csv")
    build_order_creator.create_build("HydraLingBane", "Zerg", "hydra_ling_bane.csv")
    build_order_creator.create_build("LingBane", "Zerg", "ling_bane.csv")
    build_order_creator.create_build("RavangerLingBane", "Zerg", "ravanger_ling_bane.csv")
    build_order_creator.create_build("Skytoss", "Protoss", "skytoss.csv")
    build_order_creator.create_build("ThreeCCBioTank", "Terran", "three_cc_bio_tank.csv")
    build_order_creator.create_build("TvTMech", "Terran", "tvt_mech.csv")
    build_order_creator.create_build("TwoBaseColossus", "Protoss", "two_base_colossus.csv")
    build_order_creator.create_build("TwoBaseRoach", "Zerg", "two_base_roach_timing.csv")
    build_order_creator.create_build("VoidRayGlaive", "Protoss", "voidray_to_glaive_adepts.csv")

        
    
if __name__ == "__main__":
    main()
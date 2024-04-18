from data_analysis_tools.sc2.sc2_build_order.sc2_build_order_creator import SC2BuildOrderCreator
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB
from data_analysis_tools.sc2.sc2_build_order.sc2_determine_build import SC2DetermineBuild
from database_tools.sc2.sc2_build_order_data_retriever import SC2BuildOrderDataRetriever
from replay_extraction_tools.sc2.sc2_extractor import SC2Extractor
from database_tools.sc2.sc2_replay_database import SC2ReplayDB
from database_tools.sc2.sc2_replay_data_retriever import SC2ReplayDataRetriever
def main():
    # sc2_build_order_database
    SC2BuildOrderDB.init("build_order")

    # sc2_replay_database
    SC2ReplayDB.init("replay")

    # sc2_build_order_creator
    build_order_csv = "two_base_blink.csv"
    build_order_creator = SC2BuildOrderCreator()
    build_order_creator.create_build("TwoBaseBlink", "Protoss", build_order_csv)

    # sc2_extractor
    sc2_extractor = SC2Extractor()
    sc2_extractor.run("replay_extraction_tools/tests/test_replays")

    # sc2_replay_data_retriever
    replay_data_retriever = SC2ReplayDataRetriever(SC2ReplayDB)

    # sc2_build_order_data_retriever
    build_order_data_retriever = SC2BuildOrderDataRetriever(SC2BuildOrderDB)

    # sc2_determine_build
    player_race = replay_data_retriever.get_player_race(1, 1)
    player_build = replay_data_retriever.get_commands(1,1)
    sc2_determine_build = SC2DetermineBuild(build_order_data_retriever)
    try:
        sc2_determine_build.determine_build(player_race, player_build)
    except ValueError as error:
        print(error)
        
    
if __name__ == "__main__":
    main()
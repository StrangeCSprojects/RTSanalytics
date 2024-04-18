from data_analysis_tools.sc2.sc2_analyzer import SC2Analyzer
from database_tools.sc2.sc2_build_order_data_retriever import SC2BuildOrderDataRetriever
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB
from database_tools.sc2.sc2_replay_data_retriever import SC2ReplayDataRetriever
from database_tools.sc2.sc2_replay_database import SC2ReplayDB
from server_tools.interfaces.GetBuildOrders import GetBuildOrders
from server_tools.interfaces.DisplayOverlay import DisplayOverlay
from server_tools.interfaces.GetWinratesRace import GetWinratesRace
from data_analysis_tools.sc2.sc2_build_order.sc2_build_order_overlay import (
    SC2BuildOrderOverlay,
)


class SC2ServerAPI(GetBuildOrders, DisplayOverlay, GetWinratesRace):
    """
    The server interface for interacting with SC2 RTS analytics backend functionality
    """

    def __init__(self):
        # Initialize your class attributes here if needed
        # Finish this later
        replay_data_retreiver = SC2ReplayDataRetriever(SC2ReplayDB)
        self.analyzer = SC2Analyzer()
        self.data_retriever = SC2BuildOrderDataRetriever(SC2BuildOrderDB)
        self.overlay = SC2BuildOrderOverlay()

    def get_build_orders(cls):
        # Implement the functionality to get build orders
        pass

    def display_overlay(cls):
        # Implement the functionality to display overlay
        pass

    def get_winrates_race(cls):
        # Implement the functionality to get winrates by race
        pass

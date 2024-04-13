from data_analysis_tools.general.analyzer import Analyzer
from database_tools.general.data_retriever import DataRetriever
from server_tools.interfaces.GetBuildOrders import GetBuildOrders
from server_tools.interfaces.DisplayOverlay import DisplayOverlay
from server_tools.interfaces.GetWinratesRace import GetWinratesRace
from data_analysis_tools.general.build_order.build_order_overlay import (
    BuildOrderOverlay,
)

class SC2ServerAPI(GetBuildOrders, DisplayOverlay, GetWinratesRace):
    # Declare the three class variables
    overlay: BuildOrderOverlay
    data_retriever: DataRetriever
    analyzer: Analyzer

    def __init__(cls):
        # Initialize your class attributes here if needed
        pass

    def get_build_orders(cls):
        # Implement the functionality to get build orders
        pass

    def display_overlay(cls):
        # Implement the functionality to display overlay
        pass

    def get_winrates_race(cls):
        # Implement the functionality to get winrates by race
        pass

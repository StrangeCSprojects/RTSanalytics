from server_tools.interfaces.GetBuildOrders import GetBuildOrders
from server_tools.interfaces.DisplayOverlay import DisplayOverlay
from server_tools.interfaces.GetWinratesRace import GetWinratesRace

class SC2ServerAPI(GetBuildOrders, DisplayOverlay, GetWinratesRace):
    def __init__(cls):
        # Initialize class attributes here if needed
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

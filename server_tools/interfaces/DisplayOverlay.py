from abc import ABC, abstractmethod
from data_analysis_tools.general.build_order.build_order_overlay import BuildOrderOverlay

class DisplayOverlay(ABC):
    # Define the overlay attribute
    overlay: BuildOrderOverlay

    @abstractmethod
    def display_overlay(cls):
        pass

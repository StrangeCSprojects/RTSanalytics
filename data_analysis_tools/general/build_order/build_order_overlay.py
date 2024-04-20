# Import required abstract base class (ABC) module and a general data retriever class
from abc import ABC, abstractmethod
from database_tools.general.data_retriever import DataRetriever


class BuildOrderOverlay(ABC):
    """
    An abstract base class designed to define the interface for creating
    build order overlays. This class requires subclasses to implement
    specific methods for displaying build orders in various environments
    or using different graphical libraries.
    """

    def __init__(self, data_retriever: DataRetriever) -> None:
        """
        Initializes a BuildOrderOverlay instance with a specific data retriever
        that will be used to fetch build order data from a data source.

        Parameters:
            data_retriever: An instance of DataRetriever that is capable of fetching
                            build order data from a data source such as a database or API.
        """
        super().__init__()  # Initialize the superclass (ABC)
        self.data_retriever = data_retriever  # Store the data retriever instance

    @abstractmethod
    def overlay_build(self, build_name: str) -> None:
        """
        An abstract method that must be implemented by subclasses to display
        the specified build order. This method should handle the graphical
        rendering of build order data retrieved using the `data_retriever`.

        Parameters:
            build_name: The name of the build order to display. This identifier is
                        used to retrieve the specific build order data.
        """
        pass  # This method must be overridden by subclasses

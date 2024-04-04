# Import the necessary components from the `abc` module to create an abstract base class.
from abc import ABC, abstractmethod
from data_analysis_tools.general.data_retriever import DataRetriever


class DetermineBuild(ABC):
    """
    An abstract base class designed to define a common interface for determining the build
    used in a game scenario. This class is meant to be subclassed by specific implementations
    that can determine a game entity's build based on game data or other criteria.
    """

    def __init__(self, data_retriever:DataRetriever) -> None:
        """
        Initializes a new instance of the DetermineBuild class.

        Parameters:
            data_retriever: An instance of DataRetriever used to access game data.
        """
        super().__init__()
        self.data_retriever = data_retriever


    @abstractmethod
    def determine_build(self) -> str:
        """
        The method should analyze the available data or context to identify the build and return
        a string representation of that build.

        Returns:
            str: A string identifier or description of the determined build.
        """
        pass

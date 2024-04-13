from abc import ABC, abstractmethod
from database_tools.general.data_retriever import DataRetriever


class GetBuildOrders(ABC):
    # Define the data_retriever attribute
    data_retriever: DataRetriever

    @abstractmethod
    def get_build_orders(self):
        pass

from database_tools.general.data_retriever import DataRetriever


class Analyzer:
    """
    The Analyzer class is designed to perform data analysis using data retrieved
    by an instance of the DataRetriever class. It acts as a client that consumes
    data provided by DataRetriever for various analytical tasks.
    """

    def __init__(self, data_retriever: DataRetriever) -> None:
        """
        The constructor expects an object of type DataRetriever (or any subclass thereof),
        which is then stored as an instance variable. This DataRetriever instance is used
        to fetch data that will be analyzed by the Analyzer's methods.

        Parameters:
            data_retriever (DataRetriever): An instance of DataRetriever or its subclass,
            responsible for retrieving the data to be analyzed.
        """
        # Store the provided DataRetriever instance in an instance variable.
        # This data_retriever will be used to access data for analysis.
        self.data_retriever = data_retriever

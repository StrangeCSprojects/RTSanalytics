from data_analysis_tools.general.data_retriever import DataRetriever

class Analyzer:
    def __init__(self, data_retreiver:DataRetriever) -> None:
        self.data_retriever = data_retreiver

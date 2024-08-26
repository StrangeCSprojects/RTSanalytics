from data_analysis_tools.general.analyzer import (
    Analyzer,
)  # Base class for analysis tools.
from database_tools.general.data_retriever import DataRetriever
from database_tools.sc2.sc2_replay_data_retriever import (
    SC2ReplayDataRetriever,
)  # Specific data retriever for SC2 replay data.
from data_analysis_tools.general.reports.major_battle_report import MajorBattleReport

from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB
from database_tools.sc2.sc2_build_order_data_retriever import SC2BuildOrderDataRetriever
from database_tools.sc2.sc2_replay_database import SC2ReplayDB
import logging
from config.sc2_logging_config import setup_logging

class SC2MajorBattlesAnalyzer(Analyzer):
    def __init__(self, data_retriever: DataRetriever) -> None:
        super().__init__(data_retriever)
        sc2_major_battle_report = MajorBattleReport()

    def major_battles_report(self):
        pass

    
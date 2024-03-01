from data_analysis_tools.sc2.build_order.build_type import Agressive, Standard, Economic

class RaceBuilds:
    def __init__(self, min_value_economy_standard, max_value_economy_standard, min_value_non_economy_standard, max_value_non_economy_standard
                 , min_value_economy_aggressive, max_value_economy_aggresive, min_value_non_economy_aggresive, max_value_non_economy_aggresive
                 , min_value_economy_economic, max_value_economy_economic, min_value_non_economy_economic, max_value_non_economy_ecnomic
                 ) -> None:
        self.standard_build = Standard(min_value_economy_standard, max_value_economy_standard, min_value_non_economy_standard, max_value_non_economy_standard)
        self.aggressive_build = Agressive(min_value_economy_aggressive, max_value_economy_aggresive, min_value_non_economy_aggresive, max_value_non_economy_aggresive)
        self.economic_build = Economic(min_value_economy_economic, max_value_economy_economic, min_value_non_economy_economic, max_value_non_economy_ecnomic)

class ZergBuilds(RaceBuilds):
    def __init__() -> None:
        min_value_economy_standard = 0
        max_value_economy_standard = 0
        min_value_non_economy_standard = 0
        max_value_non_economy_standard = 0
        min_value_economy_aggressive = 0
        max_value_economy_aggresive = 0
        min_value_non_economy_aggresive = 0
        max_value_non_economy_aggresive = 0
        min_value_economy_economic = 0
        max_value_economy_economic = 0
        min_value_non_economy_economic = 0
        max_value_non_economy_ecnomic = 0
        super().__init__(min_value_economy_standard, max_value_economy_standard, min_value_non_economy_standard, max_value_non_economy_standard, 
                         min_value_economy_aggressive, max_value_economy_aggresive, min_value_non_economy_aggresive, max_value_non_economy_aggresive, 
                         min_value_economy_economic, max_value_economy_economic, min_value_non_economy_economic, max_value_non_economy_ecnomic)

class ProtossBuilds(RaceBuilds):
    def __init__() -> None:
        min_value_economy_standard = 0
        max_value_economy_standard = 0
        min_value_non_economy_standard = 0
        max_value_non_economy_standard = 0
        min_value_economy_aggressive = 0
        max_value_economy_aggresive = 0
        min_value_non_economy_aggresive = 0
        max_value_non_economy_aggresive = 0
        min_value_economy_economic = 0
        max_value_economy_economic = 0
        min_value_non_economy_economic = 0
        max_value_non_economy_ecnomic = 0
        super().__init__(min_value_economy_standard, max_value_economy_standard, min_value_non_economy_standard, max_value_non_economy_standard, 
                         min_value_economy_aggressive, max_value_economy_aggresive, min_value_non_economy_aggresive, max_value_non_economy_aggresive, 
                         min_value_economy_economic, max_value_economy_economic, min_value_non_economy_economic, max_value_non_economy_ecnomic)
        
class TerranBuilds(RaceBuilds):
    def __init__() -> None:
        min_value_economy_standard = 0
        max_value_economy_standard = 0
        min_value_non_economy_standard = 0
        max_value_non_economy_standard = 0
        min_value_economy_aggressive = 0
        max_value_economy_aggresive = 0
        min_value_non_economy_aggresive = 0
        max_value_non_economy_aggresive = 0
        min_value_economy_economic = 0
        max_value_economy_economic = 0
        min_value_non_economy_economic = 0
        max_value_non_economy_ecnomic = 0
        super().__init__(min_value_economy_standard, max_value_economy_standard, min_value_non_economy_standard, max_value_non_economy_standard, 
                         min_value_economy_aggressive, max_value_economy_aggresive, min_value_non_economy_aggresive, max_value_non_economy_aggresive, 
                         min_value_economy_economic, max_value_economy_economic, min_value_non_economy_economic, max_value_non_economy_ecnomic)
class BuildType:
    def __init__(self, min_value_economy, max_value_economy, min_value_non_economy, max_value_non_economy) -> None:
        self.min_value_economy = min_value_economy
        self.max_value_economy = max_value_economy
        self.min_value_non_economy = min_value_non_economy
        self.max_value_non_economy = max_value_non_economy

class Standard(BuildType):
    def __init__(self, min_value_economy, max_value_economy, min_value_non_economy, max_value_non_economy) -> None:
        super().__init__(min_value_economy, max_value_economy, min_value_non_economy, max_value_non_economy)

class Agressive(BuildType):
    def __init__(self, min_value_economy, max_value_economy, min_value_non_economy, max_value_non_economy) -> None:
        super().__init__(min_value_economy, max_value_economy, min_value_non_economy, max_value_non_economy)

class Economic(BuildType):
    def __init__(self, min_value_economy, max_value_economy, min_value_non_economy, max_value_non_economy) -> None:
        super().__init__(min_value_economy, max_value_economy, min_value_non_economy, max_value_non_economy)

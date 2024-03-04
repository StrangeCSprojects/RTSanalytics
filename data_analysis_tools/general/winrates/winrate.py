from abc import ABC, abstractmethod


class Winrate(ABC):
    """
    Abstract Base Class to define a standard interface for calculating win rates.

    The calculate_matchup_winrates method, is expected to analyze matchups
    between different entities (e.g., players, teams, strategies) and compute win rates for
    each entity against every other entity it has faced.
    """

    @abstractmethod
    def calculate_matchup_winrates(matches: list[tuple]) -> dict:
        """
        Abstract method to calculate and return win rates for all combinations of matchups.

        Subclasses implementing this method should process a list of match results, where each
        match result is represented as a tuple.

        Parameters:
            matches (list[tuple]): A list of tuples, where each tuple contains information about
            a single match.

        Returns:
            dict: A dictionary where keys are entity identifiers, and values are dictionaries
            themselves. Each value dictionary maps opponents to win rates, representing the
            win rate of the key entity against each opponent.
        """
        pass

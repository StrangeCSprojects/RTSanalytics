from data_analysis_tools.general.analyzer import (
    Analyzer,
)  # Base class for analysis tools.
from database_tools.sc2.sc2_replay_data_retriever import (
    SC2ReplayDataRetriever,
)  # Specific data retriever for SC2 replay data.
from data_analysis_tools.general.winrates.winrate_build import (
    WinrateBuild,
)  # For calculating win rates based on builds.
from data_analysis_tools.general.winrates.winrate_race import (
    WinrateRace,
)  # For calculating win rates based on races.
from data_analysis_tools.sc2.sc2_build_order.sc2_determine_build import (
    SC2DetermineBuild,
)  # For determining SC2 build orders.

from database_tools.sc2.sc2_RTSA_DB import SC2BuildOrderDB
from database_tools.sc2.sc2_build_order_data_retriever import SC2BuildOrderDataRetriever
from database_tools.sc2.sc2_replay_database import SC2ReplayDB
import logging
from config.sc2_logging_config import setup_logging




class SC2Analyzer(Analyzer):
    """
    Specialized Analyzer class for analyzing data from an SC2 (StarCraft 2) database.
    It focuses on determining information such as build orders and win rates for different matchups.
    """

    def __init__(self, data_retriever: SC2ReplayDataRetriever) -> None:
        """
        Initializes the SC2Analyzer with a specific SC2DataRetriever.

        :param data_retriever: An instance of SC2DataRetriever to fetch game data.
        """
        super().__init__(
            data_retriever
        )  # Calls the constructor of the parent class, Analyzer.
        self.analyze_build_logger = logging.getLogger("analyze_builds")

    def winrate_build(
        self, build_order_data_retriever: SC2BuildOrderDataRetriever, build_one: str, build_two: str = "all"
    ) -> float:
        """
        Calculates win rates for different build matchups.

        Uses the data retriever to fetch all game records, then analyzes each game
        to determine the builds of each player and the winner. Compiles this information
        into matchups and calculates win rates using WinrateBuild.

        :return: A dictionary of win rates for build matchups.
        """
        winrate_calculator = (
            WinrateBuild()
        )  # Instance to calculate win rates based on builds.

        build_order_calculator = SC2DetermineBuild(
            build_order_data_retriever
        )  # Instance to determine build orders, not yet implemented.
        match_ups_list = []  # List to store matchup data for win rate calculation.

        games = self.data_retriever.get_all_games()  # Fetch all game records.

        for game in games:
            game_id = game[0]
            # Retrieve player IDs for each game.

            player_one, player_two = self.data_retriever.get_players_in_game(game_id)

            player_one_id = player_one[0]
            player_two_id = player_two[0]

            # Retrieve command lists for each player.
            player_one_commands = self.data_retriever.get_commands(
                game_id, player_one_id
            )
            player_two_commands = self.data_retriever.get_commands(
                game_id, player_two_id
            )

            # Retrieve races for each player.
            player_one_race = self.data_retriever.get_player_race(
                game_id, player_one_id
            )
            player_two_race = self.data_retriever.get_player_race(
                game_id, player_two_id
            )

            # Error handling, catches if no build order matches and if there is an incorrect build order type
            try:
                player_one_build = build_order_calculator.determine_build(
                    player_one_race, player_one_commands
                )
            except ValueError:
                msg = f"No matching build - player: {player_one_id} - game: {game_id}"
                logging.info(msg)
                continue

            # Error handling, catches if no build order matches and if there is an incorrect build order type
            try:
                player_two_build = build_order_calculator.determine_build(
                    player_two_race, player_two_commands
                )
            except ValueError:
                msg = f"No matching build - player: {player_two_id} - game: {game_id}"
                logging.info(msg)
                continue

            # Determine the winner based on game data.
            if self.data_retriever.get_winner(game_id, player_one_id):
                winner_build = player_one_build
            elif self.data_retriever.get_winner(game_id, player_two_id):
                winner_build = player_two_build
            else:
                # Error handling for cases where the winner is not determined.
                print("No winner found. Skipping game.")
                continue

            # Compile matchup data.
            match_up = (player_one_build, player_two_build, winner_build)
            match_ups_list.append(match_up)

        # Calculate and return win rates for the compiled matchups.
        result = winrate_calculator.calculate_matchup_winrates(match_ups_list, build_one, build_two)

        # error handling
        self._log_build_results(result)
        return result

    def winrate_race(self, race_one:str, race_two:str = "all") -> float:
        """
        Calculates win rates based on the races of the players in SC2 matches.

        Retrieves all games from the SC2 database, determines the races of the players in each game,
        identifies the winner's race, and calculates win rates for each race matchup.

        :return: A dictionary containing win rates for each race matchup.
        """
        winrate_calculator = WinrateRace()
        match_ups_list = []

        games = self.data_retriever.get_all_games()

        for game in games:
            game_id = game[0]
            # Retrieve player IDs and their races for the game
            player_one, player_two = self.data_retriever.get_players_in_game(game_id)

            player_one_id = player_one[0]
            player_two_id = player_two[0]

            # Retrieve races for each player.
            player_one_race = self.data_retriever.get_player_race(
                game_id, player_one_id
            )
            player_two_race = self.data_retriever.get_player_race(
                game_id, player_two_id
            )

            # Determine the winner's race based on game data
            if self.data_retriever.get_winner(game_id, player_one_id):
                winner_race = player_one_race
            elif self.data_retriever.get_winner(game_id, player_two_id):
                winner_race = player_two_race
            else:
                # Error handling for cases where the winner is not determined.
                logging.warning("No winner found... Skipping.")
                continue

            # Compile matchup data.
            match_up = (player_one_race, player_two_race, winner_race)
            match_ups_list.append(match_up)

        # Calculate and return win rates for the compiled matchups.
        result = winrate_calculator.calculate_matchup_winrates(match_ups_list, race_one, race_two)

        # error handling
        self._log_race_results(result)
        return result

    def _log_build_results(self, result: int) -> None:
        # Logs the win rate for each build order.
        msg = f"Winrate by build_order: {result}"
        self.analyze_build_logger.info(
            msg
        )  # Use the logger to output the information at the info level.

    def _log_race_results(self, result: int) -> None:
        # Logs the win rate for each race.
        msg = f"Winrate by race: {result}"
        self.analyze_build_logger.info(
            msg
        )  # Use the logger to output the information at the info level.

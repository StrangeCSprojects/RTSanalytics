from data_analysis_tools.general.winrates.winrate import Winrate


class WinrateRace(Winrate):
    def calculate_matchup_winrates(
        self, matches: list[tuple], race_one:str, race_two:str="all"
    ) -> dict:
        """
        Calculates and returns win rates for all combinations of race matchups based on the provided match outcomes.

        This method overrides the abstract method from the Winrate class, tailoring the calculation to focus on
        races. Each match result is represented as a tuple containing the races of the entities involved in the
        match and the race that won.

        Parameters:
            matches (list[tuple]): A list of tuples, where each tuple represents a match outcome. Each tuple is
            expected to contain three elements: the race of the first entity, the race of the second entity, and
            the race that won the match.

        Returns:
            dict: A nested dictionary where keys are race identifiers. Each key maps to another dictionary where
            keys are the opponent races and values are the win rates against those races. The win rates are
            represented as integer percentages.

        Example of return value structure:
            {
                'Terran': {
                    'Zerg': 50,
                    'Protoss': 45
                },
                'Zerg': {
                    'Terran': 50,
                    'Protoss': 55
                },
                ...
            }
        """
        matchups = {}

        # Initialize the matchups dictionary with each race
        for match in matches:
            for race in match[
                :2
            ]:  # match[:2] contains the two races involved in the match
                if race not in matchups:
                    matchups[race] = {}

        # Update wins and total matches for each matchup
        for race1, race2, winner in matches:
            # Ensure both races have an entry for each other
            if race2 not in matchups[race1]:
                matchups[race1][race2] = {"wins": 0, "total": 0}
            if race1 not in matchups[race2]:
                matchups[race2][race1] = {"wins": 0, "total": 0}

            # Update total match count
            matchups[race1][race2]["total"] += 1
            matchups[race2][race1]["total"] += 1

            # Update win count for the winning race
            matchups[winner][race1 if winner == race2 else race2]["wins"] += 1

        if race_two == "all":  # remove this code to revert
            # Calculate win rates for each matchup
            total_wins = 0
            total_games = 0
            win_rates = {}
            for race, opponents in matchups.items():
                if race == race_one:
                    win_rates[race] = {}
                    for opponent, record in opponents.items():
                        win_rate = (
                            (record["wins"] / record["total"]) * 100
                            if record["total"] > 0
                            else 0
                        )
                        total_wins += record["wins"]
                        total_games += record["total"]
                        win_rates[race][opponent] = int(win_rate)
            return round((total_wins / total_games) * 100, 2)

        # Calculate win rates for each matchup
        win_rates = {}
        for race, opponents in matchups.items():
            win_rates[race] = {}
            for opponent, record in opponents.items():
                win_rate = (
                    (record["wins"] / record["total"]) * 100
                    if record["total"] > 0
                    else 0
                )
                win_rates[race][opponent] = round(float(win_rate), 2)

        return win_rates[race_one][race_two]  # return win_rates to revert code

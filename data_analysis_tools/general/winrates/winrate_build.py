from data_analysis_tools.general.winrates.winrate import Winrate

class WinrateBuild(Winrate):

    def calculate_matchup_winrates(self, matches: list[tuple], build_one, build_two = "all") -> dict:
        """
        Calculates the winrates for all combinations of build types versus each other build type.

        :param matches: List of tuples with the format (build1, build2, build_that_won).
        :return: A nested dictionary with win rates for each build type against every other build type.
        """
        
        # Initialize counters for wins and total matches for each matchup
        matchups = {}
        
        for build1, build2, winner in matches:
            # Ensure both builds have an entry in the matchups dictionary
            if build1 not in matchups:
                matchups[build1] = {}
            if build2 not in matchups:
                matchups[build2] = {}
            
            # Initialize matchup record if it doesn't exist
            for build in (build1, build2):
                if build == build1:
                    opponent = build2
                else:
                    opponent = build1
                
                if opponent not in matchups[build]:
                    matchups[build][opponent] = {'wins': 0, 'total': 0}
            
            # Update total match count for both matchups
            matchups[build1][build2]['total'] += 1
            matchups[build2][build1]['total'] += 1

            matchups[winner][build1 if winner == build2 else build2]['wins'] += 1
        

        if build_two == "all":
            # Calculate win rates for each matchup
            total_wins = 0
            total_games = 0
            win_rates = {}
            for build, opponents in matchups.items():
                if build == build_one:                  
                    win_rates[build] = {}
                    for opponent, record in opponents.items():
                        win_rate = (record['wins'] / record['total']) * 100 if record['total'] > 0 else 0
                        total_wins += record["wins"]
                        total_games += record["total"]
                        win_rates[build][opponent] = int(win_rate)
            if total_games == 0:
                return 0
            return round((total_wins / total_games) * 100, 2)
                


        # Calculate win rates for each matchup
        win_rates = {}
        for build, opponents in matchups.items():
            win_rates[build] = {}
            for opponent, record in opponents.items():
                win_rate = (record['wins'] / record['total']) * 100 if record['total'] > 0 else 0
                win_rates[build][opponent] = int(win_rate)

        return win_rates[build_one][build_two] # return win_rates to revert code


        

# Import any needed modules
#
## NOT SURE WHAT MODULES WE WANT FOR THIS PARTICULAR FILE
## SO I JUST COPIED THE ONES FROM 'EXTRACTOR.PY'
import os
import sc2reader
from enum import Enum
from database_tools.sc2_database import retrieve_table_data
import random


class Stats:
    def __init__(self, game_data) -> None:
        self.game_data = game_data

        self.tvp_wins = 0
        self.tvz_wins = 0
        self.zvp_wins = 0

        self.tvp_total = 0
        self.tvz_total = 0
        self.zvp_total = 0

    def check_races_in_game(self, races: list, winner):
        set_of_races = {races[0], races[1]}
        tvp = {"Terran", "Protoss"}
        tvz = {"Terran", "Zerg"}
        zvp = {"Zerg", "Protoss"}
        winner_race = winner[0]

        if tvp.issubset(set_of_races):
            self.tvp_total += 1
            if winner_race == "Terran":
                self.tvp_wins += 1
        elif tvz.issubset(set_of_races):
            self.tvz_total += 1
            if winner_race == "Terran":
                self.tvz_wins += 1
        elif zvp.issubset(set_of_races):
            if winner_race == "Zerg":
                self.zvp_wins += 1
            self.zvp_total += 1
        else:
            print("ERROR in check_races_in_game")

    def wr_race(self):
        for game in self.game_data:
            races = game[0]
            winner = game[1]
            self.check_races_in_game(races, winner)
        tvp_wr = round((self.tvp_wins / self.tvp_total) * 100, 2)
        tvz_wr = round((self.tvz_wins / self.tvz_total) * 100, 2)
        zvp_wr = round((self.zvp_wins / self.zvp_total) * 100, 2)
        return (tvp_wr, tvz_wr, zvp_wr)


def main():
    """Main entry point"""

    # Generate random races and winners for testing
    def generate_dummy_game_data(num_games):
        races = ["Terran", "Protoss", "Zerg"]
        game_data = []
        for _ in range(num_games):
            race1 = random.choice(races)
            race2 = random.choice([race for race in races if race != race1])
            winner = random.choice([race1, race2])
            game_data.append(([race1, race2], [winner]))
        return game_data

    # Generate 1000 dummy games for testing
    game_data = generate_dummy_game_data(1000)
    # print(game_data)

    # Instantiate Stats object with the generated dummy data
    stats = Stats(game_data)

    # Calculate and print win rates
    print(stats.tvp_total)
    print("Win rates:")
    print(f"Terran vs Protoss:{stats.wr_race()[0]}%")
    print(f"Terran vs Zerg:{stats.wr_race()[1]}%")
    print(f"Zerg vs Protoss: {stats.wr_race()[2]}%")


# Interpret this module
if __name__ == "__main__":
    main()

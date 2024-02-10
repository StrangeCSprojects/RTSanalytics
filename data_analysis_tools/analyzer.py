
# Import any needed modules
#
## NOT SURE WHAT MODULES WE WANT FOR THIS PARTICULAR FILE
## SO I JUST COPIED THE ONES FROM 'EXTRACTOR.PY'
import os
import sc2reader
from enum import Enum
from database_tools.sc2_database import retrieve_table_data

def winrate_by_race():
    games = retrieve_table_data('games')

    zerg_wins_vs_protoss = 0
    zerg_wins_vs_terran = 0
    terran_wins_vs_protoss = 0

    zvp_total = 0
    zvt_total = 0
    tvp_total = 0

    for game in games:
        if 'Zerg' in game and 'Protoss' in game:
            zvp_total += 1
            if game[6] == game[1]:
                if game[2] == 'Zerg':
                    zerg_wins_vs_protoss += 1
            elif game[6] == game[3]:
                if game[4] == 'Zerg':
                    zerg_wins_vs_protoss += 1
        elif 'Zerg' in game and 'Terran' in game:
            zvt_total += 1
            if game[6] == game[1]:
                if game[2] == 'Zerg':
                    zerg_wins_vs_terran += 1
            elif game[6] == game[3]:
                if game[4] == 'Zerg':
                    zerg_wins_vs_terran += 1
        elif 'Teran' in game and 'Protoss' in game:
            tvp_total += 1
            if game[6] == game[1]:
                if game[2] == 'Terran':
                    terran_wins_vs_protoss += 1
            elif game[6] == game[3]:
                if game[4] == 'Terran':
                    terran_wins_vs_protoss += 1
    print(zerg_wins_vs_protoss)
    print(zerg_wins_vs_terran)
    print(terran_wins_vs_protoss)
    print(zvp_total)
    print(zvt_total)
    print(tvp_total)






def main():
    """Main entry point"""
    # print("\nPRINTING DATA IN 'GAMES' TABLE...")
    # row = retrieve_table_data('games', 1) # Get just a single row of data
    # table_data = retrieve_table_data('games') # Retrieve all the data from 'games' table
    # for row in table_data:
    #     print(row)
    #     for data in row:
    #         print(data)
    #     print()

    test = (1,2,3)
    print(test[0])
    winrate_by_race()

# Interpret this module
if __name__ == "__main__":
    main()

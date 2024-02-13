
# Import any needed modules
#
## NOT SURE WHAT MODULES WE WANT FOR THIS PARTICULAR FILE
## SO I JUST COPIED THE ONES FROM 'EXTRACTOR.PY'
import os
import sc2reader
from enum import Enum
from database_tools.sc2_database import insert_into_db, retrieve_table_data

def main():
    """Main entry point"""

    print("\nPRINTING DATA IN 'GAMES' TABLE...")
    row = retrieve_table_data('games', 1) # Get just a single row of data
    table_data = retrieve_table_data('games') # Retrieve all the data from 'games' table
    for row in table_data:
        print(row)
    print('\n')
    for data in row:
        print(data)    

# Interpret this module
if __name__ == "__main__":
    main()

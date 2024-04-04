"""
    This is a python script used for easier
    debugging, testing, and experimenting
"""

# Import any needed modules
from database_tools.sc2.sc2_data_retriever import SC2DataRetriever
from replay_extraction_tools.sc2.sc2_extractor import SC2Extractor
from database_tools.sc2.sc2_database import SC2ReplayDB
import csv


def main():
    """
    Main entry point
    """

    with open("test.csv", 'r') as csv_file:
        csv_file = csv.reader(csv_file)
        next(csv_file, None)
        for i in csv_file:
            print(i)
        # print(csv_file.read())



# Interpret this module
if __name__ == "__main__":
    main()

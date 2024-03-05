
## THESE WILL BE USED IN FUTURE BUILDS
# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import declarative_base, relationship
# import sc2reader

# OUR MVP WILL USE THESE
import sqlite3
from typing import Tuple


class SC2_DB:
    """A class for managing SC2 database"""
    # Initialize class variables
    _db_file_path = "database_tools/sc2_games.db"

    @staticmethod
    def create_tables() -> None:
        """
        Initializes all the tables if they do not already exist
    
        Parameters:
        - None
    
        Returns:
        - None
        """
        
        # Get connected to the database
        conn = sqlite3.connect(SC2_DB._db_file_path)
        cursor = conn.cursor()

        # In future builds, this will iterate through all the
        # required table names and create them one-by-one
        if not SC2_DB._table_exists('games', conn):
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS games (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    player1_name TEXT,
                    player1_race TEXT,
                    player2_name TEXT,
                    player2_race TEXT,
                    game_mode TEXT,
                    winner TEXT
                );
            """)
            
            # Commit the change               
            conn.commit()
        
        # Close the connection after the tables have been initialized
        conn.close()


    @staticmethod
    def _table_exists(table_name: str, conn: sqlite3.Connection) -> bool:
        """
        Check if a table exists in the database.

        Parameters:
        - table_name - (str): The name of the table to check.
        - conn - SQLite connection: Manages the connection to the database
            and allows for querying for specific Star Craft II data.

        Returns:
        - bool: True if the table exists, False otherwise.
        """

        # Return true if cursor objects finds the table and false otherwise
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        result = cursor.fetchone() is not None
        return result


    @staticmethod
    def _get_column_count(table_name: str, conn: sqlite3.Connection) -> int:
        """Gets the number of columns in a database table"""
        # Create a cursor object with the database connection
        cursor = conn.cursor()

        # Execute SQL query to get table definition
        cursor.execute(f"PRAGMA table_info({table_name})")

        # Fetch all rows from the result
        rows = cursor.fetchall()

        # Count the number of rows, which represents the number of columns
        column_count = len(rows)
    
        # Return the number of columns
        return column_count


    @staticmethod
    def insert_into_db(table_name: str, new_game_data: Tuple[str, ...]) -> None:
        """
        Inserts game data into a specified table and does not insert the data
            if the specified table does not exist

        Parameters:
        - table_name - string: The name of the table to insert the game data 
        - new_game_data - Tuple(str): A tuple containing the field values to be inserted

        Returns:
        - None
        """
        # Connect to SQLite database (creates a new database file if not exists)
        conn = sqlite3.connect(SC2_DB._db_file_path)

        # Create a cursor to execute SQL commands
        cursor = conn.cursor()

        # Check if the number of columns matchsthe length of the new game data
        num_fields = len(new_game_data)
        if num_fields != SC2_DB._get_column_count(table_name, conn) - 1: # Ignores the "ID" field in any table
            print("Invalid number of fields. Make sure table columns and new data match in length.")
            return None
    
        # Dynamically construct the SQL statement to insert the data
        placeholders = ', '.join(['?' for _ in range(num_fields)])
        sql = f"INSERT INTO {table_name} VALUES (NULL, {placeholders})"
    
        # Execute the constructed sql statement with cursor
        cursor.execute(sql, new_game_data)
    
        # Commit the changes to the database
        conn.commit()
    
        # Close the connection
        print("Insert data success!")
        conn.close()

    @staticmethod
    def retrieve_table_data(table_name: str, game_id: str = None) -> list[Tuple[str]]:
        """
        Retrieves the data from a specified table
    
        Parameters:
        - table_name - string: A string representation of a table name
            in the database (not case-sensitive)
        - game_id - string: A string representing the ID of a specific
            row in the table (set to None by default)
    
        Returns:
        - If game_id is not specified, a tuple containing the data for each
                row in the specified table is returned in the following format:
                    [
                        (
                            GAME ID,
                            PLAYER 1 NAME, PLAYER 1 RACE,
                            PLAYER 2 NAME, PLAYER 2 RACE,
                            GAME MODE, WINNER NAME
                        )
                    ]
                otherwise, the function returns a tuple containing the data
                    for the specified row.
        """
        # Connect to SQLite database (creates a new database file if not exists)
        conn = sqlite3.connect(SC2_DB._db_file_path)

        # Create a cursor to execute SQL commands
        cursor = conn.cursor()

        # A result variable which contains one of three types: None, tuple, or list of tuples
        result = None

        # Check if table exists and return data if true, otherwise return None
        if not SC2_DB._table_exists(table_name, conn):
            print("No such table exists. Sorry!")
            return result # This particular return statement will change in future builds
        elif game_id is not None:
            cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", str(game_id))
            result = cursor.fetchone()
        else:
            cursor.execute(f"SELECT * FROM {table_name}")
            result = cursor.fetchall()

        # Close the connection and return the result
        conn.close()
        return result
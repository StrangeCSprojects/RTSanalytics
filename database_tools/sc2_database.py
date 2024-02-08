
## THESE WILL BE USED IN FUTURE BUILDS
# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import declarative_base, relationship
# import sc2reader

# OUR MVP WILL USE THESE
import sqlite3
from typing import Tuple

def check_table_existence(table_name: str, conn) -> bool:
    """
    Check if a table exists in the database.

    Parameters:
    - table_name - (str): The name of the table to check.
    - conn - SQLite connection: Manages the connection to the database
        and allows for querying for specific Star Craft II data.

    Returns:
    - bool: True if the table exists, False otherwise.
    """
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    return cursor.fetchone() is not None

def insert_into_db(new_game_data: tuple([str, str, str, str, str, str])) -> None:
    """
    Inserts game data into the 'games' table

    Parameters:
    - new_game_data - Tuple(str): A tuple containing the field values to be inserted

    Returns:
    - None
    """
    # Connect to SQLite database (creates a new database file if not exists)
    conn = sqlite3.connect('database_tools/sc2_games.db')

    # Create a cursor to execute SQL commands
    cursor = conn.cursor()

    # Create a table to store game data if the table does not exist
    if not check_table_existence('games', conn):
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

    # Insert the data into the table
    cursor.execute("""
        INSERT INTO games (player1_name, player1_race, player2_name, player2_race, game_mode, winner)
        VALUES (?, ?, ?, ?, ?, ?)
    """, new_game_data)

    # Commit the changes to the database
    conn.commit()
    
    # Close the connection
    conn.close()


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
    conn = sqlite3.connect('database_tools/sc2_games.db')

    # Create a cursor to execute SQL commands
    cursor = conn.cursor()
    
    # A result variable which contains one of three types: None, tuple, or list of tuples
    result = None
    
    # Check if table exists and return data if true, otherwise return None
    if not check_table_existence(table_name, conn):
        print("No such table exists. Sorry!")
        return result # This particular return statement will change in future builds
    elif game_id:
        cursor.execute(f"SELECT * FROM {table_name} WHERE rowid = ?", str(game_id))
        result = cursor.fetchone()
    else:
        cursor.execute(f"SELECT * FROM {table_name}")
        result = cursor.fetchall()
    
    # Close the connection and return the result
    conn.close()
    return result








# KEEP IGNORING THIS PART


# Base = declarative_base()

# class Map(Base):
#     __tablename__ = 'maps'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)

# class Player(Base):
#     __tablename__ = 'players'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     race = Column(String)

#     map_id = Column(Integer, ForeignKey('maps.id'))
#     map = relationship('Map', back_populates='players')

# class Game(Base):
#     __tablename__ = 'games'

#     id = Column(Integer, primary_key=True)
#     mode = Column(String)
#     winner = Column(String)

#     map_id = Column(Integer, ForeignKey('maps.id'))
#     map = relationship('Map', back_populates='games')

# Map.players = relationship('Player', back_populates='map')
# Map.games = relationship('Game', back_populates='map')

# # Create an SQLite database engine
# engine = create_engine('sqlite:///starcraft.db')

# # Create tables
# Base.metadata.create_all(engine)

# def insert_game_data(replay_file):
#     # Load the replay file
#     replay = sc2reader.load_replay(replay_file)

#     # Create a session
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     # Insert data into the 'maps' table
#     map_data = Map(name=replay.map_name)
#     session.add(map_data)
#     session.commit()

#     # Insert data into the 'players' table
#     for player in replay.players:
#         player_data = Player(name=player.name, race=player.play_race, map=map_data)
#         session.add(player_data)

#     # Determine the winner and insert data into the 'games' table
#     winner = max(replay.teams, key=lambda team: team.result).players[0].name
#     game_data = Game(mode=replay.real_type, winner=winner, map=map_data)
#     session.add(game_data)

#     # Commit changes
#     session.commit()

# # Replace 'example.SC2Replay' with the path to your replay file
# insert_game_data("example.SC2Replay")

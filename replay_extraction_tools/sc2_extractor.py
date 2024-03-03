# Import any needed modules
from imaplib import Commands
import os
from re import S
from sys import platlibdir
from typing import Self
import sc2reader
from database_tools.sc2_database import SC2_DB
from replay_extraction_tools.extractor import Extractor
from database_tools.general_database_access import DataStorage
from database_tools.sc2_database_access import (
    CommandDataStorage,
    PlayDataStorage,
    PlayerDataStorage,
    IssuesDataStorage,
    GameDataStorage,
)


class SC2Extractor(Extractor):
    """
    Extracts, filters, and pushes data from replays
    to a database
    """

    def __init__(self, folder_path: str) -> None:
        """
        SC2Extractor constructor
        """
        super().__init__(folder_path)

        self._game_data = GameDataStorage()

        self._commands_one = CommandDataStorage()
        self._play_one = PlayDataStorage()
        self._player_one = PlayerDataStorage()
        self._issues_one = IssuesDataStorage()

        self._commands_two = CommandDataStorage()
        self._play_two = PlayDataStorage()
        self._player_two = PlayerDataStorage()
        self._issues_two = IssuesDataStorage()

        self._player_id = 0
        self._command_id = 0
        self._game_id = 0

    def extract(self) -> dict:
        """
        extract data from a group of replays and return a dictionary of replay data
        """
        replay_container = {}
        replay_counter = 0

        # Getting replays from folder
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path):
                # Filling replay dictionary
                replay_counter += 1
                # print(f"Loading replay {replay_counter}.....   ")
                replay = sc2reader.load_replay(file_path, load_map=True)
                # print(type(replay))
                # print(dir(replay))
                replay_container[replay_counter] = replay

        return replay_container

    def filter_into_tables(self, replay_container: dict) -> None:
        """
        Filter relevant data from a group of replays and store that information into
        a group of tables then return a list of those tables.
        """

        for replay_key in replay_container:
            replay = replay_container[replay_key]

            # Create unique game and player IDs
            game_id = SC2_DB._create_game_id()
            player_one_id = SC2_DB._create_player_id()
            player_two_id = SC2_DB._create_player_id()

            # Players data
            player_one = replay.players[0]
            player_two = replay.players[1]

            # Player names
            player_one_name = player_one.name
            player_two_name = player_two.name

            # Player races
            player_one_race = player_one.play_race
            player_two_race = player_two.play_race

            # Get command data for both players (This may become its own function post-mvp)
            player_one_commands = []
            player_two_commands = []
            for event in replay.events:
                if isinstance(event, sc2reader.events.game.CommandEvent):
                    command_time = event.second
                    command_name = event.ability_name
                    if event.player.name == player_one_name:
                        player_one_commands.append((command_time, command_name))
                    else:
                        player_two_commands.append((command_time, command_name))

            # Game data
            game_map = replay.map_name
            game_mode = replay.attributes.get(16).get("Game Mode")
            if not replay.winner:
                winner_id = -1  # This game will not get stored
            else:
                for player in replay.players:
                    if player.result == "Win":
                        winner_name = player.name
                        if winner_name == player_one_name:
                            winner_id = player_one_id
                        else:
                            winner_id = player_two_id

            # Create data records and store them into appropriate storage
            # units, starting with the command data
            player_one_commands_id = SC2_DB._create_command_id()
            player_two_commands_id = SC2_DB._create_command_id()

            commands_one_record = (player_one_commands_id, player_one_commands)
            commands_two_record = (player_two_commands_id, player_two_commands)

            self._commands_one.set_data(commands_one_record)
            self._commands_two.set_data(commands_two_record)

            # Game data
            game_data_record = (game_id, game_map, game_mode, winner_id)
            self._game_data.set_data(game_data_record)

            # Player one data
            play_one_record = (game_id, player_one_id)
            player_one_record = (player_one_id, player_one_race, player_one_name)

            self._play_one.set_data(play_one_record)
            self._player_one.set_data(player_one_record)

            # Player Two data
            play_two_record = (game_id, player_two_id)
            player_two_record = (player_two_id, player_two_race, player_two_name)

            self._play_two.set_data(play_two_record)
            self._player_two.set_data(player_two_record)

            # Issued data
            issued_player_one = (player_one_commands_id, player_one_id, game_id)
            issued_player_two = (player_two_commands_id, player_two_id, game_id)

            self._issues_one.set_data(issued_player_one)
            self._issues_two.set_data(issued_player_two)

    def _get_tables(self) -> list[DataStorage]:
        return [
            self._player_one,
            self._player_two,
            self._commands_one,
            self._commands_two,
            self._game_data,
            self._issues_one,
            self._issues_two,
            self._play_one,
            self._play_two,
        ]

    def run(self) -> None:
        return super().run()

    def _batch_insert(self, table_list: list[DataStorage]) -> None:
        return super()._batch_insert(table_list)

    def build_order(self):
        pass


# # Build order types
# class BuildOrder(Enum):
#     UNKNOWN = 0
#     AGRESSION = 1
#     STANDARD = 2
#     ECONOMY = 3

# def replay_analysis(player_name, folder_path):
#     """Gather data to determine winrate based on race"""
#     replay_counter = 0

#     # Loop through all files in the folder
#     for filename in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, filename)
#         if os.path.isfile(file_path):

#             replay_counter +=1
#             print(f"Loading replay {replay_counter}.....   ")
#             replay = sc2reader.load_replay(file_path, load_map=True)

#             # Access basic information
#             game_mode = replay.attributes.get(16).get("Game Mode")

#             # Players
#             player_one = replay.players[0]
#             player_two = replay.players[1]

#             # Player names
#             player_one_name = player_one.name
#             player_two_name = player_two.name

#             # Player races
#             player_one_race = player_one.play_race
#             player_two_race = player_two.play_race

#             # Game winner name
#             if replay.winner:
#                 for player in replay.players:
#                     if player.result == 'Win':
#                         winner_name = player.name

#             # Determine build order
#             print(f"Player Name: {player_name}\nGame Mode: {game_mode}\nPlayer One: {player_one_name} - {player_one_race}\nPlayer Two: {player_two_name} - {player_two_race}\nWinner: {winner_name}\n")
#             build_order(replay)

#             # Store game data into sc2_overlay database
#             new_record = (
#                 player_one_name,
#                 player_one_race,
#                 player_two_name,
#                 player_two_race,
#                 game_mode,
#                 winner_name
#             )
#             SC2_DB.insert_into_db('games', new_record)


# def build_order(replay):
#     """Determine build order"""
#     command_center_count = 1
#     production_building_count = 0
#     build_order = BuildOrder.UNKNOWN

#     # Initialize a dictionary to hold events for each player
#     player_events = {player: [] for player in replay.players}

#     # Iterate through events and process only unit events
#     for event in replay.events:
#         if isinstance(event, sc2reader.events.UnitInitEvent):
#             player = event.unit.owner
#             if player:
#                 player_events[player].append(event)

#     for player, events in player_events.items():
#         if player.name == "Cstrange":
#             print(f"Events for Player {player.name}:")
#             for event in events:

#                 game_speed_factor = 1.4
#                 real_time_seconds = int(event.second / game_speed_factor)
#                 # print(f" - {event.unit.name} at {int(real_time_seconds // 60)}.{real_time_seconds % 60}s")
#                 if event.unit.name == "OrbitalCommand" or event.unit.name == "OrbitalCommandFlying" :
#                     command_center_count += 1
#                 elif event.unit.name == "Barracks":
#                     production_building_count += 1
#                 elif event.unit.name == "Factory":
#                     production_building_count += 1
#                 elif event.unit.name == "Starport":
#                     production_building_count += 1

#                 if event.second < 300:
#                     if command_center_count >= 3:
#                         build_order = BuildOrder.ECONOMY
#                     elif production_building_count >= 7:
#                         build_order = BuildOrder.AGRESSION
#                     elif command_center_count == 2 and production_building_count < 7:
#                         build_order = BuildOrder.STANDARD
#     # print(command_center_count)
#     # print(production_building_count)
#     print(f"Build Order: {build_order.name}")

# def build_order(self, replay):
#     """Determine build order"""
#     command_center_count = 1
#     production_building_count = 0
#     build_order = BuildOrder.UNKNOWN

#     # Initialize a dictionary to hold events for each player
#     player_events = {player: [] for player in replay.players}

#     # Iterate through events and process only unit events
#     for event in replay.events:
#         if isinstance(event, sc2reader.events.UnitInitEvent):
#             player = event.unit.owner
#             if player:
#                 player_events[player].append(event)

#     for player, events in player_events.items():
#         if player.name == "Cstrange":
#             print(f"Events for Player {player.name}:")
#             for event in events:
#                 game_speed_factor = 1.4
#                 real_time_seconds = int(event.second / game_speed_factor)
#                 # print(f" - {event.unit.name} at {int(real_time_seconds // 60)}.{real_time_seconds % 60}s")
#                 if (
#                     event.unit.name == "OrbitalCommand"
#                     or event.unit.name == "OrbitalCommandFlying"
#                 ):
#                     command_center_count += 1
#                 elif event.unit.name == "Barracks":
#                     production_building_count += 1
#                 elif event.unit.name == "Factory":
#                     production_building_count += 1
#                 elif event.unit.name == "Starport":
#                     production_building_count += 1

#                 if event.second < 300:
#                     if command_center_count >= 3:
#                         build_order = BuildOrder.ECONOMY
#                     elif production_building_count >= 7:
#                         build_order = BuildOrder.AGRESSION
#                     elif command_center_count == 2 and production_building_count < 7:
#                         build_order = BuildOrder.STANDARD
#     # print(command_center_count)
#     # print(production_building_count)
#     print(f"Build Order: {build_order.name}")

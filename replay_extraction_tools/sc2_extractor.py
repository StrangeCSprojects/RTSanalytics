# Import any needed modules
import os
import sc2reader
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

        # Tables in sc2 database

        # THIS FOLLOWING CODE CAN BE MADE ACCESSIBLE
        # FROM WITHIN THE SC2_DB CLASS
        #
        # START
        self.game = GameDataStorage()

        self.commands_one = CommandDataStorage()
        self.play_one = PlayDataStorage()
        self.player_one = PlayerDataStorage()
        self.issues_one = IssuesDataStorage()

        self.commands_two = CommandDataStorage()
        self.play_two = PlayDataStorage()
        self.player_two = PlayerDataStorage()
        self.issues_two = IssuesDataStorage()

        self.player_id = 0
        self.command_id = 0
        self.game_id = 0
        # END

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
                print(f"Loading replay {replay_counter}.....   ")
                replay = sc2reader.load_replay(file_path, load_map=True)
                print(type(replay))
                print(dir(replay))
                replay_container[replay_counter] = replay

        return replay_container

    def filter_into_tables(self, replay_container: dict) -> None:
        """
        Filter relevant data from a group of replays and store that information into
        a group of tables then return a list of those tables.
        """

        for replay_key in replay_container:
            replay = replay_container[replay_key]

            game_id = self.create_game_id()
            player_one_id = self.create_player_id()
            player_two_id = self.create_player_id()

            # Access basic information
            game_mode = replay.attributes.get(16).get("Game Mode")

            # Players
            player_one = replay.players[0]
            player_two = replay.players[1]

            # Player names
            player_one_name = player_one.name
            player_two_name = player_two.name

            # Player races
            player_one_race = player_one.play_race
            player_two_race = player_two.play_race

            # Game winner name
            if replay.winner:
                for player in replay.players:
                    if player.result == "Win":
                        winner_name = player.name

            # NEEDS TO BE FILLED WITH DATA ONCE DATABASE IS CREATED!!!
            self.game.set_data()

            # Player one data
            self.play_one.set_data()
            self.player_one.set_data()
            self.commands_one.set_data()
            self.issues_one.set_data()

            # Player two data
            self.play_two.set_data()
            self.player_two.set_data()
            self.commands_two.set_data()
            self.issues_two.set_data()

    def get_tables(self) -> list[DataStorage]:
        return [
            self.game,
            self.play_one,
            self.player_one,
            self.commands_one,
            self.issues_one,
            self.play_two,
            self.player_two,
            self.commands_two,
            self.issues_two,
        ]

    def run(self) -> None:
        return super().run()

    def batch_insert(self, table_list: list[DataStorage]) -> None:
        return super().batch_insert(table_list)

    # ID generation
    def create_game_id(self) -> int:
        """Increment and return game id"""
        self.game_id += 1
        return self.game_id

    def create_player_id(self) -> int:
        """Increment and return player id"""
        self.player_id += 1
        return self.player_id

    def create_command_id(self) -> int:
        """Increment and return command id"""
        self.command_id += 1
        return self.command_id


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

# Import any needed modules
import os
import sc2reader
from sqlalchemy import true, false
from replay_extraction_tools.extractor import Extractor
from database_tools.sc2.sc2_database import SC2_DB
from database_tools.general.general_database_access import DataStorage
from database_tools.sc2.sc2_database_access  import (
    PlayDataStorage,
    PlayerDataStorage,
    GameDataStorage,
)


class SC2Extractor(Extractor):
    """
    Extracts, filters, and pushes data from replays
    to a database
    """

    def __init__(self) -> None:
        """
        SC2Extractor constructor
        """
        super().__init__()

        self._player_data = PlayerDataStorage()
        self._game_data = GameDataStorage()
        self._play_data = PlayDataStorage()

    def extract(self) -> dict:
        """
        extract data from a group of replays and return a dictionary of replay data
        """
        replay_container = {}
        replay_counter = 0

        # Getting replays from folder
        for filename in os.listdir(self.folder_path):
            print(filename)
            file_path = os.path.join(self.folder_path, filename)
            print(file_path)
            if os.path.isfile(file_path):
                # Filling replay dictionary
                replay_counter += 1

                try:
                    replay = sc2reader.load_replay(file_path, load_map=True)
                    print("Success!")
                    print()
                except Exception as e:
                    print(f"Failed to load replay {file_path}: {e}")

                replay_container[replay_counter] = replay

        return replay_container

    def filter_into_tables(self, replay_container: dict) -> None:
        """
        Filter relevant data from a group of replays and store that information into
        a group of tables then return a list of those tables.
        """

        for replay_key in replay_container:


            replay = replay_container[replay_key]
            if not replay.winner:
                continue  # We are only storing games where there is a winner
            
            # Players data
            player_one = replay.players[0]
            player_two = replay.players[1]

            # Player names
            player_one_name = player_one.name
            player_two_name = player_two.name


            # Get player and game IDs
            game_id = SC2_DB._create_game_id()
            player_one_info = self._player_data._get_player_from_storage(player_one_name)
            if player_one_info:
                player_one_id = player_one_info["player_id"]
            else:
                player_one_id = SC2_DB._create_player_id()
            player_two_info = self._player_data._get_player_from_storage(player_two_name)
            if player_two_info:
                player_two_id = player_two_info["player_id"]
            else:
                player_two_id = SC2_DB._create_player_id()

            # Player races
            player_one_race = player_one.play_race
            player_two_race = player_two.play_race

            # Get command data for both players (This may become its own function post-mvp)
            player_one_commands = []
            player_two_commands = []
            for event in replay.events:
                # Adjustment for sc2's longer seconds
                time_adjustment = 1.4

                # Process unit, building, and upgrade commands
                if (event.name in ("UnitBornEvent", "UnitInitEvent")) and (event.second > 0):
                    # Adjust time to correct for in-game time scale
                    command_time = event.second // time_adjustment

                    command_type = event.name
                    command_name = event.unit.name
                    
                    # Determine which player executed the command and append to their list
                    if event.unit_controller.name == player_one_name:
                        player_one_commands.append(((command_type, command_name), command_time))
                    else:
                        player_two_commands.append(((command_type, command_name), command_time))

                # Process upgrade commands
                elif (hasattr(event, 'upgrade_type_name')) and (event.second > 0):
                    # Adjust time to correct for in-game time scale
                    command_time = event.second // time_adjustment
                    
                    command_type = event.name
                    command_name = event.upgrade_type_name

                    # Determine which player executed the command and append to their list
                    if event.player.name == player_one_name:
                        player_one_commands.append(((command_type, command_name), command_time))
                    else:
                        player_two_commands.append(((command_type, command_name), command_time))

            # Game data
            game_map = replay.map_name
            game_mode = replay.attributes.get(16).get("Game Mode")
            for player in replay.players:
                if player.result == "Win":
                    if player.name == player_one_name:
                        player_one_wins = True
                    else:
                        player_one_wins = False
                    break  # No need to check the other player if player one is the winner

            print(f"Replay {replay_key}")
            print(f"Player one: {player_one_name}\n\trace: {player_one_race}\n\twinner?: {player_one_wins}")
            print(f"Player_two_name: {player_two_name}\n\trace: {player_two_race}\n\twinner?: {not player_one_wins}")
            print()

            # Create data records and store them into appropriate units
            # Player one data
            play_one_record = (
                game_id,
                player_one_id,
                player_one_race,
                player_one_wins,
                player_one_commands,
            )
            player_one_record = (player_one_id, player_one_name)

            self._play_data.set_data(play_one_record)
            self._player_data.set_data(player_one_record)

            # Player Two data
            play_two_record = (
                game_id,
                player_two_id,
                player_two_race,
                (not player_one_wins),
                player_two_commands,
            )
            player_two_record = (player_two_id, player_two_name)

            self._play_data.set_data(play_two_record)
            self._player_data.set_data(player_two_record)

            # Game data
            game_data_record = (game_id, game_map, game_mode)
            self._game_data.set_data(game_data_record)

    def _get_tables(self) -> list[DataStorage]:
        return [
            self._player_data,
            self._game_data,
            self._play_data
        ]

    def run(self, folder_path: str) -> None:
        super().run(folder_path)

    def _batch_insert(self, table_list: list[DataStorage]) -> None:
        return super()._batch_insert(table_list)

SC2_DB.init("sc2_db")
extractor = SC2Extractor()
extractor.run("replay_extraction_tools/replays")
# Import any needed modules
import os
import sc2reader
from replay_extraction_tools.General.extractor import Extractor
from database_tools.sc2.sc2_replay_database import SC2ReplayDB
from database_tools.general.general_database_access import DataStorage
from database_tools.sc2.sc2_database_access import (
    PlayDataStorage,
    PlayerDataStorage,
    GameDataStorage,
)
import logging


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
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path) and file_path.endswith(".SC2Replay"):
                # Filling replay dictionary
                replay_counter += 1

                # Check file loads properly
                try:
                    replay = sc2reader.load_replay(file_path, load_map=True)
                except Exception:
                    logging.warning(f"File: {file_path} - File failed to load")

                replay_container[replay_counter] = replay

            else:
                # Check file opens properly
                logging.warning("File not found or File isn't of type .SC2Replay")

        return replay_container

    @staticmethod
    def _process_commands(replay: sc2reader.resources.Replay, p1, p2):
        # Get command data for both players
        p1_name = p1.name
        p1_commands = []
        p2_commands = []
        for event in replay.events:
            # Adjustment for sc2's longer seconds
            time_adjustment = 1.4

            # Process unit and building commands
            if (
                hasattr(event, "unit")
                and hasattr(event, "unit_controller")
                and event.unit is not None
            ) and (event.second > 0):
                # Adjust time to correct for in-game time scale
                command_time = event.second // time_adjustment

                command_type = event.name
                command_name = event.unit.name

                # Determine which player executed the command and append to their list
                if event.unit_controller.name == p1_name:
                    p1_commands.append(((command_type, command_name), command_time))
                else:
                    p2_commands.append(((command_type, command_name), command_time))

            # Process upgrade commands
            elif (hasattr(event, "upgrade_type_name")) and (event.second > 0):
                # Adjust time to correct for in-game time scale
                command_time = event.second // time_adjustment

                command_type = event.name
                command_name = event.upgrade_type_name

                # Determine which player executed the command and append to their list
                if event.player.name == p1_name:
                    p1_commands.append(((command_type, command_name), command_time))
                else:
                    p2_commands.append(((command_type, command_name), command_time))
        return p1_commands, p2_commands

    def filter_into_tables(self, replay_container: dict) -> None:
        """
        Filter relevant data from a group of replays and store that information into
        a group of tables then return a list of those tables.
        """

        for replay in replay_container.values():
            if not replay.winner or len(replay.players) != 2:
                logging.warning(
                    f"Player Count: {replay.players} - Replay may not have a winner"
                )
                continue  # We are only storing games where there is a winner and two players

            # Process data for both players
            player_one = replay.players[0]
            player_two = replay.players[1]

            # Player names
            player_one_name = player_one.name
            player_two_name = player_two.name

            # Get player and game IDs
            game_id = SC2ReplayDB._create_game_id()
            player_one_info = self._player_data._get_player_from_storage(
                player_one_name
            )
            if player_one_info:
                player_one_id = player_one_info["player_id"]
            else:
                player_one_id = SC2ReplayDB._create_player_id()
            player_two_info = self._player_data._get_player_from_storage(
                player_two_name
            )
            if player_two_info:
                player_two_id = player_two_info["player_id"]
            else:
                player_two_id = SC2ReplayDB._create_player_id()

            # Player races
            player_one_race = player_one.play_race
            player_two_race = player_two.play_race

            # Process commands and store them in lists
            player_one_commands, player_two_commands = SC2Extractor._process_commands(
                replay, player_one, player_two
            )

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
            game_data_record = (game_id, game_mode, game_map)
            self._game_data.set_data(game_data_record)

    def _get_tables(self) -> list[DataStorage]:
        return [self._player_data, self._game_data, self._play_data]

    def run(self, folder_path: str) -> None:
        super().run(folder_path)

    def _batch_insert(self, table_list: list[DataStorage]) -> None:
        super()._batch_insert(table_list)

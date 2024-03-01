
from abc import ABC, abstractmethod
from database_tools.general_database_access import Table

class Extractor(ABC):
    """
    Abstract class that extracts data from a group of replays, filters the data into
    table classes and inserts that data into a database.
    """
    def __init__(self, folder_path: str) -> None:
        # super().__init__()
        self.folder_path = folder_path


    @abstractmethod
    def extract(self) -> None:
        pass


    @abstractmethod
    def filter_into_tables(self) -> None:
        pass


def build_order(replay):
    """Determine build order"""
    command_center_count = 1
    production_building_count = 0
    build_order = BuildOrder.UNKNOWN

    # Initialize a dictionary to hold events for each player
    player_events = {player: [] for player in replay.players}

    # Iterate through events and process only unit events
    for event in replay.events:
        if isinstance(event, sc2reader.events.UnitInitEvent):
            player = event.unit.owner
            if player:
                player_events[player].append(event)

    for player, events in player_events.items():
        if player.name == "Cstrange":
            print(f"Events for Player {player.name}:")
            for event in events:

                game_speed_factor = 1.4
                real_time_seconds = int(event.second / game_speed_factor)
                # print(f" - {event.unit.name} at {int(real_time_seconds // 60)}.{real_time_seconds % 60}s")
                if event.unit.name == "OrbitalCommand" or event.unit.name == "OrbitalCommandFlying" :
                    command_center_count += 1
                elif event.unit.name == "Barracks":
                    production_building_count += 1
                elif event.unit.name == "Factory":
                    production_building_count += 1
                elif event.unit.name == "Starport":
                    production_building_count += 1
                
                if event.second < 300:
                    if command_center_count >= 3:
                        build_order = BuildOrder.ECONOMY
                    elif production_building_count >= 7:
                        build_order = BuildOrder.AGRESSION
                    elif command_center_count == 2 and production_building_count < 7:
                        build_order = BuildOrder.STANDARD
    # print(command_center_count)
    # print(production_building_count)
    print(f"Build Order: {build_order.name}")

    def batch_insert(self, table_list:list[Table]) -> None:
        for table in table_list:
            table.push()


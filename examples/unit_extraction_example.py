import sc2reader

def extract(file_path) -> None:
    """
    extract data from a replay
    """
    replay = sc2reader.load_replay(file_path, load_map=True) # load a replay

    print(replay.players) # Players in game

    for event in replay.events:
        if (
            hasattr(event, "unit")
            and hasattr(event, "unit_controller")
            and event.unit is not None
            ) and (event.second > 0) and (event.unit_controller.name == "Cstrange"):
            
            # print(event.name) # unit type
            # print(event.unit.name) # unit name
            # print(event.second) # time unit was created

            
            # command_time = event.second // 1.4 # Adjust time to correct for in-game time scale
            # time = f"{int(command_time // 60)}.{int((command_time % 60))}"
            print((event.name, event.unit.name))
            # print(event.unit_controller.name) # Player name who created the unit
        # if (
        #     hasattr(event, "upgrade_type_name")
        #     ) and (event.second > 0):
            
        #     # print(event.name) # unit type
        #     # print(event.unit.name) # unit name
        #     # print(event.second) # time unit was created

            
        #     # command_time = event.second // 1.4 # Adjust time to correct for in-game time scale
        #     # time = f"{int(command_time // 60)}.{int((command_time % 60))}"
        #     print((event.name, event.upgrade_type_name))
        #     # print(event.unit_controller.name) # Player name who created the unit

file_path = "examples/sc2_replays/zerg_unit_types.SC2Replay"
extract(file_path)




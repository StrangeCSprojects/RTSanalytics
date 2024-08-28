import sc2reader

def extract(file_path) -> None:
    """
    extract all of the units that have died and their death timers
    """
    replay = sc2reader.load_replay(file_path, load_map=True) # load a replay

    print(replay.players) # Players in game

    worthless_units = ["Larva", "Egg", "Broodling", "Locust", "Mule"]


    # gets all of the "Unit Died" events while ignoring ones for things like Broodlings or Larva taht have no resource value
    unit_deaths = [
        event for event in replay.events 
        if event.name == "UnitDiedEvent" and not any(worthless_unit in str(event.unit) for worthless_unit in worthless_units)
    ]

    for event in unit_deaths:
        print(event)
        print(event.second)

file_path = "examples/sc2_build_replays/Standard Game.SC2Replay"


extract(file_path)




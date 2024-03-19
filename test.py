import sc2reader

# Load your replay
replay = sc2reader.load_replay(
    "replay_extraction_tools/replays/UpgradeGathering.SC2Replay"
)

print(replay.type)
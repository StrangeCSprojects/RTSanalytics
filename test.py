import sc2reader

# Load your replay
replay = sc2reader.load_replay('replay_extraction_tools/replays/UpgradeGathering.SC2Replay')

# Iterate through the events in the replay
for event in replay.events:

        # if (hasattr(event, 'unit') and event.unit is not None) and (event.name != "UnitDoneEvent") and (event.second > 0):

        #     time_adjustments = event.second //1.4

        #     unit_name = event.unit.name
        #     print(f"{event.name} : {unit_name} {int(time_adjustments // 60)}.{int(time_adjustments % 60)}")
        
        if (hasattr(event, 'upgrade_type_name')) and (event.second > 0) and (event.upgrade_type_name not in ("SprayTerran", "SprayProtoss", "SprayZerg")):
            time_adjustments = event.second //1.4

            unit_name = event.upgrade_type_name
            print(f"{event.name} : {unit_name} {int(time_adjustments // 60)}.{int(time_adjustments % 60)}")

from data_analysis_tools.sc2.sc2_analyzer import SC2Analyzer
from database_tools.sc2.sc2_build_order_data_retriever import SC2BuildOrderDataRetriever
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB
from database_tools.sc2.sc2_replay_data_retriever import SC2ReplayDataRetriever
from database_tools.sc2.sc2_replay_database import SC2ReplayDB
from server_tools.interfaces.get_build_orders import GetBuildOrders
from server_tools.interfaces.display_overlay import DisplayOverlay
from server_tools.interfaces.get_winrates_race import GetWinratesRace
from data_analysis_tools.sc2.sc2_build_order.sc2_build_order_overlay import (
    SC2BuildOrderOverlay,
)
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all domains on all routes

# Initialize your class attributes here if needed
SC2ReplayDB.init("replay")
SC2BuildOrderDB.init("build_order")
replay_data_retreiver = SC2ReplayDataRetriever(SC2ReplayDB)
data_retriever = SC2BuildOrderDataRetriever(SC2BuildOrderDB)
analyzer = SC2Analyzer(replay_data_retreiver)

overlay = SC2BuildOrderOverlay(data_retriever)

@app.route('/get_build_orders')
def get_build_orders():
    # Implement the functionality to get build orders
    build_data = data_retriever.get_all_builds()
    build_list = []
    for build in build_data:
        flutter_build = {"name": build[0], "race": build[1], "winrate": analyzer.winrate_build(data_retriever, build[0])}

        build_list.append(flutter_build)

    return jsonify(build_list)

@app.route('/display_overlay')
def display_overlay():
# Implement the functionality to display overlay
    build_name = request.args.get('build_name')
    print(build_name)
    overlay.overlay_build(f"{build_name}")

@app.route('/get_winrates_race')
def get_winrates_race():
# Implement the functionality to get winrates by race
    terran = analyzer.winrate_race("Terran")
    protoss = analyzer.winrate_race("Protoss")
    zerg = analyzer.winrate_race("Zerg")
    return jsonify({'terran':float(terran), 'protoss':float(protoss), 'zerg':float(zerg)})


if __name__ == "__main__":
    app.run(debug=True, port=5010)
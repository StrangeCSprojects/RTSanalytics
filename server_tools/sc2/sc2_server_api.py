from data_analysis_tools.sc2.sc2_analyzer import SC2Analyzer
from database_tools.sc2.sc2_build_order_data_retriever import SC2BuildOrderDataRetriever
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB
from database_tools.sc2.sc2_replay_data_retriever import SC2ReplayDataRetriever
from database_tools.sc2.sc2_replay_database import SC2ReplayDB
from server_tools.interfaces.GetBuildOrders import GetBuildOrders
from server_tools.interfaces.DisplayOverlay import DisplayOverlay
from server_tools.interfaces.GetWinratesRace import GetWinratesRace
from data_analysis_tools.sc2.sc2_build_order.sc2_build_order_overlay import (
    SC2BuildOrderOverlay,
)
from flask import Flask, jsonify

app = Flask(__name__)

# Initialize your class attributes here if needed
SC2ReplayDB.init("replay")
SC2BuildOrderDB.init("build_order")
replay_data_retreiver = SC2ReplayDataRetriever(SC2ReplayDB)
data_retriever = SC2BuildOrderDataRetriever(SC2BuildOrderDB)
analyzer = SC2Analyzer(replay_data_retreiver)

# self.overlay = SC2BuildOrderOverlay()

@app.route('/get_build_orders')
def get_build_orders():
    # Implement the functionality to get build orders
    # build_data = data_retriever.get_all_builds()
    # build_list = []
    # for build in build_data:
    #     build_list.append(build[0])

    return jsonify(["1","2"])

# @app.route('/display_overlay')
# def display_overlay(self):
# # Implement the functionality to display overlay
#     pass

# @app.route('/get_winrates_race')
# def get_winrates_race(self):
# # Implement the functionality to get winrates by race
#     output = self.analyzer.winrate_race()
#     return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True, port=5010)

from data_analysis_tools.general.build_order.build_order_overlay import BuildOrderOverlay
from database_tools.sc2.sc2_build_order_data_retriever import SC2BuildOrderDataRetriever
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB
import tkinter as tk
import pygetwindow as gw

class SC2BuildOrderOverlay(BuildOrderOverlay):
    def __init__(self, data_retriever: SC2BuildOrderDataRetriever) -> None:
        super().__init__(data_retriever)

    def overlay_build(self, build_name: str) -> None:
        build = self.data_retriever.get_build_by_name(build_name)
        build_commands = build[1]

        # Create the main window
        root = tk.Tk()
        root.title(build_name)

        # Set the window to be always on top
        root.attributes('-topmost', True)
        # Set the window transparency (0.0 fully transparent, 1.0 fully opaque)
        root.attributes('-alpha', 0.7)

        # Create a frame to contain the list
        frame = tk.Frame(root, bg='white')
        frame.pack(padx=100, pady=10)

        # Add tuples to the frame
        for command in build_commands:
            unit_name = command[0][0][1]
            unit_time = int(command[0][1])
            command_tuple = (unit_name, self._convert_seconds(unit_time))
            label = tk.Label(frame, text=str(command_tuple), bg='white')
            label.pack()

        root.protocol("WM_DELETE_WINDOW")

        # Start the Tkinter event loop
        root.mainloop()

    def _convert_seconds(self, seconds):
        minutes = seconds // 60  # Get the whole minutes
        remaining_seconds = seconds % 60  # Get the leftover seconds
        return round(minutes + remaining_seconds/100,2)
    
SC2BuildOrderDB.init("builds_db")

dr = SC2BuildOrderDataRetriever(SC2BuildOrderDB)

test = SC2BuildOrderOverlay(dr)

test.overlay_build("GreedyLurkers")
# Import required modules for the overlay functionality
from data_analysis_tools.general.build_order.build_order_overlay import (
    BuildOrderOverlay,
)
from database_tools.sc2.sc2_build_order_data_retriever import SC2BuildOrderDataRetriever
from database_tools.sc2.sc2_build_order_database import SC2BuildOrderDB
import tkinter as tk
import pygetwindow as gw


class SC2BuildOrderOverlay(BuildOrderOverlay):
    """
    Provides a graphical overlay for StarCraft II build orders. This class
    retrieves build order data from a database and displays it in a transparent
    overlay window that remains on top of other applications.
    """

    def __init__(self, data_retriever: SC2BuildOrderDataRetriever) -> None:
        """
        Initializes the SC2BuildOrderOverlay object by passing the data retriever
        to its superclass, which handles the general overlay creation.
        """
        super().__init__(data_retriever)

    def overlay_build(self, build_name: str) -> None:
        """
        Retrieves and displays a specified build order in a GUI overlay. The
        build order includes commands specific to StarCraft II units and timings.

        Parameters:
            build_name: The name of the build order to be displayed.
        """
        # Retrieve the build order data from the database using the provided build name
        build = self.data_retriever.get_build_by_name(build_name)
        build_commands = build[1]

        # Create and configure the main window of the overlay
        root = tk.Tk()
        root.title(build_name)  # Set the window title to the build name
        root.attributes("-topmost", True)  # Window remains on top
        root.attributes("-alpha", 0.7)  # Set window transparency to 70%

        # Set up a frame to list all build commands
        frame = tk.Frame(root, bg="white")
        frame.pack(padx=100, pady=10)

        # Populate the frame with labels for each build command
        for command in build_commands:
            unit_name = command[0][0][1]  # Extract the unit name from the command
            unit_time = int(
                command[0][1]
            )  # Extract the command time and convert to integer
            command_tuple = (unit_name, self._convert_seconds(unit_time))  # Format time
            label = tk.Label(frame, text=str(command_tuple), bg="white")  # Create label
            label.pack()

        # Initialize the event loop for the GUI
        root.mainloop()

    def _convert_seconds(self, seconds):
        """
        Converts seconds into a formatted string representing minutes and seconds.

        Parameters:
            seconds: The number of seconds to convert.

        Returns:
            A formatted string representing the time in minutes and fractional seconds.
        """
        minutes = seconds // 60  # Convert total seconds to minutes
        remaining_seconds = seconds % 60  # Calculate remaining seconds
        return f"{minutes}:{remaining_seconds:02}"  # Format and return as string

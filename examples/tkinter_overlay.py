import tkinter as tk
import pygetwindow as gw

def create_overlay(tuples):
    # Create the main window
    root = tk.Tk()
    root.title("Tuple Overlay")

    # Set the window to be always on top
    root.attributes('-topmost', True)
    # Set the window transparency (0.0 fully transparent, 1.0 fully opaque)
    root.attributes('-alpha', 0.7)

    # Create a frame to contain the list
    frame = tk.Frame(root, bg='white')
    frame.pack(padx=100, pady=10)

    # Add tuples to the frame
    for tup in tuples:
        label = tk.Label(frame, text=str(tup), bg='white')
        label.pack()

    # # Prevent the window from being closed easily
    # def on_closing():
    #     pass  # Do nothing

    root.protocol("WM_DELETE_WINDOW")

    # Start the Tkinter event loop
    root.mainloop()

# Example tuples
tuples = [(1, 2), (3, 4), (5, 6)]
create_overlay(tuples)

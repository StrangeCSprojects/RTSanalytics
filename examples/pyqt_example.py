from PyQt5 import QtWidgets, QtCore, QtGui
import psutil
import time
class OverlayWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.set_initial_style()

    def init_ui(self):
        # Set layout
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        # Create list widget to display tuples
        self.list_widget = QtWidgets.QListWidget()
        self.layout.addWidget(self.list_widget)

        # Add sample data
        sample_tuples = [("Marine", "00:15"), ("SCV", "00:20"), ("Barracks", "00:45")]
        for item_text in sample_tuples:
            item = QtWidgets.QListWidgetItem(f"{item_text[0]} - {item_text[1]}")
            self.list_widget.addItem(item)

        # Set window properties to make it topmost, frameless, and input-transparent
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowTransparentForInput)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def set_initial_style(self):
        """Apply initial styling with translucent border and background."""
        self.setStyleSheet("""
            QWidget {
                color: white;
                font-size: 12px;
                font-weight: bold;
                padding: 10px;
            }
            QListWidget {
                background-color: rgba(0, 0, 0, 0.3);  /* Semi-transparent black background */
            }
            QListWidgetItem {
                color: white;  /* White text for list items */
            }
        """)
            
def wait_for_sc2():
    sc2_process_name = "SC2_x64.exe"  # This might vary, especially on different platforms or versions
    while True:
        # Check if SC2 is running
        if sc2_process_name in (p.name() for p in psutil.process_iter()):
            print("StarCraft II has started!")
            time.sleep(5)
            break
        else:
            print("Waiting for StarCraft II to start...")
            time.sleep(5)  # Check every 5 seconds

    return True

def create_overlay():
    wait_for_sc2()
    app = QtWidgets.QApplication([])
    window = OverlayWindow()
    window.setGeometry(1700, 100, 200, 150)  # Set position and size
    window.show()
    app.exec_()
create_overlay()
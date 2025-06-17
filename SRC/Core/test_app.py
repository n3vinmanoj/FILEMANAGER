import sys
import os

print(">>> Bootstrapping...")


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
print(f">>> Project root resolved as: {project_root}")

if project_root not in sys.path:
    sys.path.insert(0, project_root)
    print(">>> Project root added to sys.path")
else:
    print(">>> Project root already in sys.path")


try:
    from SRC.UI.py.main_window_ui import Ui_MainWindow
    print(">>> Successfully imported Ui_FileManagerWindow")
except Exception as e:
    print(f"!!! Failed to import UI: {e}")
    raise

from PySide6.QtWidgets import QApplication, QMainWindow


class TestWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        print(">>> Initializing TestWindow...")
        self.setupUi(self)
        print(">>> UI setup complete")
        self.setWindowTitle("File Manager Test")
        self.setMinimumSize(800, 600)
        self.show()
        print(">>> Window shown")


if __name__ == "__main__":
    print(">>> Starting QApplication...")
    app = QApplication(sys.argv)

    try:
        print(">>> Creating window instance...")
        window = TestWindow()
        print(">>> Entering app event loop...")
        app.exec()
        print(">>> Event loop exited")
    except Exception as e:
        print(f"!!! Exception occurred: {e}")
import sys
import os

# Add project root to sys.path so imports work
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from PySide6.QtWidgets import QApplication, QMainWindow
from SRC.UI.py.main_window_ui import Ui_FileManagerWindow

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print(">>> Creating UI object")
        self.ui = Ui_FileManagerWindow()
        self.ui.setupUi(self)  # Properly setup this QMainWindow
        print(">>> UI setup complete")

        # Optional: Set window title and size
        self.setWindowTitle("File Manager Test")
        self.setMinimumSize(800, 600)
        self.show()

if __name__ == "__main__":
    print(">>> Starting app...")
    app = QApplication(sys.argv)
    window = TestWindow()
    print(">>> Running event loop...")
    app.exec()
    print(">>> Event loop exited")

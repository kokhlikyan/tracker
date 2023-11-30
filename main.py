import os
import sys
from PySide6.QtWidgets import QApplication
from ui.tracker import ExpenseTracker


def main():
    window = ExpenseTracker()
    window.show()
    return window


if __name__ == '__main__':
    # load dlls used by cairo
    app_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    os.environ["PATH"] += os.pathsep + app_path  # for Windows
    os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = app_path  # for macOS
    os.environ["LD_LIBRARY_PATH"] = app_path  # for Linux
    app = QApplication(sys.argv)
    w = main()

    sys.exit(app.exec())

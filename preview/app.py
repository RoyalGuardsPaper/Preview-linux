"""Application startup and Qt application configuration."""

import sys

from PySide6.QtWidgets import QApplication

from preview.main_window import MainWindow


def main() -> int:
    """Create the application window and run Qt's event loop."""
    application = QApplication(sys.argv)
    application.setApplicationName("Preview")
    application.setApplicationVersion("0.1.0")

    window = MainWindow()
    window.show()

    return application.exec()

"""The main window shown when Preview starts."""

from PySide6.QtWidgets import QLabel, QMainWindow


class MainWindow(QMainWindow):
    """A small starting point for the Preview user interface."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Preview")
        self.resize(900, 650)

        welcome = QLabel("Preview is ready. Image and PDF viewing are coming next.")
        welcome.setWordWrap(True)
        welcome.setContentsMargins(24, 24, 24, 24)
        self.setCentralWidget(welcome)

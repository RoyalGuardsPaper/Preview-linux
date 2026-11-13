"""Basic checks for creating the application's main window."""

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication

from preview.main_window import MainWindow


def test_main_window_has_expected_title() -> None:
    application = QApplication.instance() or QApplication([])
    window = MainWindow()

    assert window.windowTitle() == "Preview"
    assert window.centralWidget() is not None

    window.close()
    application.quit()

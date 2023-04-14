from PySide6.QtWidgets import QMainWindow
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyChat")

    def closeEvent(self, event) -> None:
        os._exit(0)
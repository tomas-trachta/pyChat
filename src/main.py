from PySide6.QtWidgets import QApplication
from src.controller.appController import AppController


if __name__ == "__main__":
    app = QApplication()
    appController = AppController()
    app.exec()
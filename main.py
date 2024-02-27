from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

from business_logic.api.base_requests import ApiRequests
from business_logic.api.qt_login_controller import QtLoginController
from Config import Config

from pages.Login import Login

class Navigator:
    config: Config
    requests: ApiRequests
    navigation_queue: list

    def __init__(self, window):
        self._window = window

    def navigate(self, obj):
        print(obj)
        obj._navigator = self
        obj._config = self.config
        obj._requests = self.requests

        if obj.layout is None:
            obj.layout = QVBoxLayout()

        obj.markup()
        print("end markup", obj)

        widget = QWidget()
        widget.setLayout(obj.layout)

        self._window.setCentralWidget(widget)
        print("end", obj)
        

    def add_page_to_queue(self, page):
        self.navigation_queue.append(page)


app = QApplication([])
window = QMainWindow()

window.setWindowTitle("Power Control")
window.setFixedSize(265, 370)

if __name__ == "__main__":
    navigator = Navigator(window)

    config = Config()
    navigator.config = config

    requests = QtLoginController(config, navigator)
    navigator.requests = requests

    navigator.navigate(Login())

    window.show()
    app.exec()

# python -m main
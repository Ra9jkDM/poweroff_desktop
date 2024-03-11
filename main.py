from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from business_logic.api.base_requests import ApiRequests
import business_logic.general_storage as Storage
from pages.Login import Login


class Navigator:
    navigation_queue: list = []

    def __init__(self, window):
        self._window = window

    def navigate(self, obj):
        if obj.layout is None:
            obj.layout = QVBoxLayout()

        obj.markup()

        widget = QWidget()
        widget.setLayout(obj.layout)

        self._window.setCentralWidget(widget)

        if len(self.navigation_queue) > 0:
            page = self.navigation_queue[0]
            del self.navigation_queue[0]
            self.navigate(page)


    # in need navigation in func 'markup'
    def add_page_to_queue(self, page): 
        self.navigation_queue.append(page)


app = QApplication([])
window = QMainWindow()

def configure_app():
    window.setWindowTitle("Power Control")
    window.setFixedSize(265, 370)

    navigator = Navigator(window)

    storage = Storage.Storage()
    storage.set_navigator(navigator)
    storage.set_login_page(Login())

    navigator.navigate(Login())

if __name__ == "__main__":
    configure_app()

    window.show()
    app.exec()

    
# python -m main
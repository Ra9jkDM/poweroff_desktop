from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

from Pages.Login import Login

class Navigator:
    def __init__(self, window):
        self._window = window

    def navigate(self, obj):
        obj._navigator = self

        if obj.layout is None:
            obj.layout = QVBoxLayout()

        obj.markup()

        widget = QWidget()
        widget.setLayout(obj.layout)

        self._window.setCentralWidget(widget)


app = QApplication([])
window = QMainWindow()

window.setWindowTitle("Power Control")
window.setFixedSize(215, 350)

if __name__ == "__main__":
    navigator = Navigator(window)
    navigator.navigate(Login())

    window.show()
    app.exec()

# python -m main
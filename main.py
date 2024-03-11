from PyQt6.QtWidgets import QApplication, QMainWindow
import business_logic.general_storage as Storage
from pages.Login import Login
from Navigator import Navigator


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
from business_logic.singleton import Singleton

from Config import Config
from business_logic.api.qt_login_controller import QtLoginController

class Storage(Singleton):
    _init_state = False

    def __init__(self):
        if not self._init_state:
            self._init_state = True
            
            self.config = Config()
            self.requests = QtLoginController(self.config)

    def set_navigator(self, navigator):
        self.navigator = navigator

    def set_login_page(self, page):
        self.requests.set_login_page(lambda: self.navigator.navigate(page))

if __name__ == "__main__":
    s = Storage()
    print(s)
    s1 = Storage()
    print(s1)
from business_logic.singlethon import Singlethon

from Config import Config
from business_logic.api.qt_login_controller import QtLoginController

class Storage(Singlethon):
    def __init__(self):
        self.config = Config()
        self.requests = QtLoginController(self.config)

    def set_navigator(self, navigator):
        self.navigator = navigator

    def set_login_page(self, page):
        self.requests.set_login_page(lambda: self.navigator.navigate(page))
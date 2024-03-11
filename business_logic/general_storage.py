from singlethon import Singlethon

from Config import Config
from business_logic.api.qt_login_controller import QtLoginController

class Storage(Singlethon):
    def __init__(self):
        self.config = Config()
        self.requests = QtLoginController(config)

    def set_navigator(self, navigator):
        self.navigator = navigator
        self.requests.set_navigator(self.navigator)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QGridLayout

from IPage import IPage
from Config import Config
from BaseWidgets import create_title, create_image

import pages.Login as Login
import pages.Sessions as Sessions

from business_logic.api.requests.power import shutdown, reboot

class Power(IPage):
    image_size = QSize(200, 200)

    def __init__(self):
        super().__init__()
        self.config = self._storage.config
        self.layout = QGridLayout()

    def markup(self):
        title = self.create_title()
        image = self.create_image()

        shutdown = self.create_shutdown_button()
        reboot = self.create_reboot_button()

        sessions = self.create_sessions_button()
        logout = self.create_logout_button()


        self.layout.addWidget(title, 0, 0, 1, 2)
        self.layout.addWidget(image, 1, 0, 1, 2)

        self.layout.addWidget(shutdown, 2, 0, 1, 2)
        self.layout.addWidget(reboot, 3, 0, 1, 2)
        
        self.layout.addWidget(logout, 4, 0)
        self.layout.addWidget(sessions, 4, 1)

    def create_title(self):
        title = create_title(self.config.name)
        return title

    def create_image(self):
        return create_image(self.config.image_path, self.image_size)

    def create_shutdown_button(self):
        button = QPushButton("Shutdown")
        button.clicked.connect(lambda: shutdown())
        return button

    def create_reboot_button(self):
        button = QPushButton("Reboot")
        button.clicked.connect(lambda: reboot())
        return button

    def create_logout_button(self):
        self.logout = QPushButton("Logout")
        self.logout.clicked.connect(lambda: self._logout())
        return self.logout

    def create_sessions_button(self):
        self.sessions = QPushButton("Sessions")
        self.sessions.clicked.connect(lambda: self._sessions())
        return self.sessions

    def _logout(self):
        self._storage.requests.logout()
        self._storage.navigator.navigate(Login.Login())

    def _sessions(self):
        self._storage.navigator.navigate(Sessions.Sessions())

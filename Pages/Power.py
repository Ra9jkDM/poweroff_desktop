from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QGridLayout

from IPage import IPage
from Config import Config
from BaseWidgets import create_title, create_image

import Pages.Login as Login
import Pages.Sessions as Sessions


class Power(IPage):
    image_size = QSize(200, 200)

    def __init__(self, config: Config):
        self.config = config
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
        # Todo
        return button

    def create_reboot_button(self):
        button = QPushButton("Reboot")
        # Todo
        return button

    def create_logout_button(self):
        self.logout = QPushButton("Logout")
        self.logout.clicked.connect(lambda: self._logout())
        return self.logout

    def _logout(self):
        self._navigator.navigate(Login.Login())

    def create_sessions_button(self):
        self.sessions = QPushButton("Sessions")
        self.sessions.clicked.connect(lambda: self._sessions())
        return self.sessions

    def _sessions(self):
        self._navigator.navigate(Sessions.Sessions(self.config))
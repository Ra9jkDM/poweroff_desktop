from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap

from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox

from IPage import IPage
from Config import Config
from BaseWidgets import create_image, _create_pixmap

import pages.Power as Power



class Login(IPage):
    image_size = QSize(200, 200)
    
    def markup(self):
        self.config = Config()

        image = self.create_image()
        servers = self.create_combobox()
        login = self.create_login()
        password = self.create_password()
        submit = self.create_login_button()

        widgets = [image, servers, login, password, submit]
        self.add_widgets(widgets)

    def create_image(self):
        self.image = create_image(self.config.image_path, self.image_size)
        return self.image

    def _create_pixmap(self, img_path):
        return _create_pixmap(img_path, self.image_size)

    def create_combobox(self):
        self.combo = QComboBox()
        self.combo.addItems(self.config.api_names)
        self.combo.currentIndexChanged.connect(lambda x: self._api_changed(x))
        return self.combo

    def _api_changed(self, id):
        self.config.api_id = id
        pixmap = self._create_pixmap(self.config.image_path)
        self.image.setPixmap(pixmap)

    def create_login(self):
        self.login = QLineEdit()
        self.login.setPlaceholderText("Login")
        return self.login

    def create_password(self):
        self.pwd = QLineEdit()
        self.pwd.setPlaceholderText("Password")
        self.pwd.setEchoMode(QLineEdit.EchoMode.Password)
        return self.pwd

    def create_login_button(self):
        self.button = QPushButton("Login")
        self.button.clicked.connect(lambda: self._login())
        return self.button

    def _login(self):
        print("Login action")
        print(f"Login: {self.login.text()}\nPassword: {self.pwd.text()}") 
        print("Api url:"+self.config.url)

        # Todo

        self._navigator.navigate(Power.Power(self.config))
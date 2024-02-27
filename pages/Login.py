from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap

from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox

from IPage import IPage
from BaseWidgets import create_image, _create_pixmap

from business_logic.api.model import User

import pages.Power as Power



class Login(IPage):
    image_size = QSize(200, 200)
    
    def markup(self):
        r = self._requests.is_logged_in()
        print(r, r==True)
        if True:
            print("fo")
            # self._navigator.navigate(Power.Power(self._config))
            power = Power.Power(self._config)
            power.markup()
            self.layout = power.layout
            return

        image = self.create_image()
        servers = self.create_combobox()
        login = self.create_login()
        login.setText("bob")
        password = self.create_password()
        password.setText("pwd123")
        submit = self.create_login_button()

        widgets = [image, servers, login, password, submit]
        self.add_widgets(widgets)

    def create_image(self):
        self.image = create_image(self._config.image_path, self.image_size)
        return self.image

    def _create_pixmap(self, img_path):
        return _create_pixmap(img_path, self.image_size)

    def create_combobox(self):
        self.combo = QComboBox()
        self.combo.addItems(self._config.api_names)
        self.combo.currentIndexChanged.connect(lambda x: self._api_changed(x))
        return self.combo

    def _api_changed(self, id):
        self._config.api_id = id
        pixmap = self._create_pixmap(self._config.image_path)
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
        print("Api url:"+self._config.url)


        user = User(username=self.login.text(), password=self.pwd.text())
        
        if self._requests.login(user):
            self._navigator.navigate(Power.Power(self._config))

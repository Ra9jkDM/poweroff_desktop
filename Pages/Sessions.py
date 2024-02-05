from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QGridLayout

from IPage import IPage
from Config import Config
from BaseWidgets import create_title, create_image

import Pages.Power as Power


class Sessions(IPage):

    def __init__(self, config: Config):
        self.config = config

    def markup(self):
        title = create_title("Sessions")
        back = self.create_back_button()

        # Todo scrolling list of elements with "Delete" buttons

        widgets = [title, back]
        self.add_widgets(widgets)



    def create_back_button(self):
        back = QPushButton("Back")
        back.clicked.connect(lambda: self._back())
        return back

    def _back(self):
        self._navigator.navigate(Power.Power(self.config))
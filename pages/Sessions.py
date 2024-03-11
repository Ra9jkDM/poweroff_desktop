from PyQt6.QtCore import Qt, QSize, QMargins
from PyQt6.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit, 
            QComboBox, QHBoxLayout, QVBoxLayout, QGridLayout, QScrollArea)
import json
from datetime import datetime

from IPage import IPage

from BaseWidgets import create_title, create_image
from models.SessionDTO import SessionDTO
from business_logic.api.requests.user import delete_tokens

import pages.Power as Power


class Sessions(IPage):

    def markup(self):
        title = create_title("Sessions")
        delete = self.create_delete_all_button()
        back = self.create_back_button()


        tokens = self._storage.requests.get_token_list()
        tokens = tokens.content.decode("utf-8")
        tokens = json.loads(tokens)

        self.tokens = tokens

        mas=[]
        for i in tokens:
            session = self._convert(i)

            obj = self.create_session_widget(session)
            if session.current:
                mas.insert(0, obj)
            else:
                mas.append(obj)

        self.sessions = self.create_list_of_widgets(mas)

        self.area = self.create_scroll_area(self.sessions)

        widgets = [title, self.area, delete, back]
        self.add_widgets(widgets)



    def create_back_button(self):
        back = QPushButton("Back")
        back.clicked.connect(lambda: self._back())
        return back

    def _back(self):
        self._storage.navigator.navigate(Power.Power())

    def create_delete_all_button(self):
        delete = QPushButton("Delete all except active")
        delete.clicked.connect(lambda: self._delete_all())
        return delete

    def create_scroll_area(self, widget):
        area = QScrollArea()
        area.setWidget(widget)
        area.setWidgetResizable(True)
        return area

    def create_list_of_widgets(self, widgets: list):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        widget.setLayout(layout)

        for i in widgets:
            layout.addWidget(i)

        return widget
        

    def create_session_widget(self, session: SessionDTO):
        widget = QWidget()
        if session.current:
            widget.setStyleSheet('background-color: #ffe0b6;')

        layout = QHBoxLayout()
        margins = QMargins(0,5,5,0)
        layout.setContentsMargins(margins)

        date = QLabel(session.date)
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(lambda: self._delete_one(widget, session.id))

        layout.addWidget(date)
        layout.addWidget(delete_button)
        
        widget.setLayout(layout)
        return widget

    def _convert(self, obj):
        session = SessionDTO(id=obj["id"], 
            date=datetime.strptime(obj['creation_date'][:-7], "%Y-%m-%dT%H:%M:%S").strftime("%d %b, %Y - %H:%M"), 
            current=obj['current'])
        return session

    def _delete_one(self, widget, id):
        # print(f"Delete {id}")
        delete_tokens([id])
        layout = self.sessions.layout()
        widget.setParent(None)

    def _delete_all(self):
        # print("Delete all")
        all_id = []
        active = None

        for i in self.tokens:
            if not i["current"]:
                all_id.append(i["id"])
            else:
                active = i

        delete_tokens(all_id)
        self.tokens = []

        if active:
            layout = self.sessions.layout()
            for i in range(layout.count())[::-1]:
                layout.itemAt(i).widget().setParent(None)


            session = self._convert(active)
            session = self.create_session_widget(session)
            self.sessions.layout().addWidget(session)
            



if __name__=="__main__":
    from main import Navigator, window, app
    navigator = Navigator(window)
    navigator.navigate(Sessions([]))
    window.show()
    app.exec()

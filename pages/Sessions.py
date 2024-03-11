from PyQt6.QtCore import Qt, QSize, QMargins
from PyQt6.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit, 
            QComboBox, QHBoxLayout, QVBoxLayout, QGridLayout, QScrollArea)

from IPage import IPage

from BaseWidgets import create_title, create_image
from models.SessionDTO import SessionDTO

import pages.Power as Power


class Sessions(IPage):

    def markup(self):
        title = create_title("Sessions")
        delete = self.create_delete_all_button()
        back = self.create_back_button()

        mas=[]
        for i in range(10):
            session = SessionDTO(id=i, date=f"{i} Feb, 2024 - 12:28")
            mas.append(self.create_session_widget(session))

        self.sessions = self.create_list_of_widgets(mas)

        area = self.create_scroll_area(self.sessions)

        widgets = [title, area, delete, back]
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

    def _delete_all(self):
        print("Delete all")

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

    def _delete_one(self, widget, id):
        print(f"Delete {id}")
        layout = self.sessions.layout()
        widget.setParent(None)
        # widget.hide()
        # layout.removeWidget(widget)

if __name__=="__main__":
    from main import Navigator, window, app
    navigator = Navigator(window)
    navigator.navigate(Sessions([]))
    window.show()
    app.exec()

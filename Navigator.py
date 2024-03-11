from PyQt6.QtWidgets import QWidget, QVBoxLayout

class Navigator:
    navigation_queue: list = []

    def __init__(self, window):
        self._window = window

    def navigate(self, obj):
        if obj.layout is None:
            obj.layout = QVBoxLayout()

        obj.markup()

        widget = QWidget()
        widget.setLayout(obj.layout)

        self._window.setCentralWidget(widget)

        if len(self.navigation_queue) > 0:
            page = self.navigation_queue[0]
            del self.navigation_queue[0]
            self.navigate(page)


    # in need navigation in func 'markup'
    def add_page_to_queue(self, page): 
        self.navigation_queue.append(page)
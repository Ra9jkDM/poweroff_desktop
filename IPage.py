import business_logic.general_storage as Storage

class IPage:
    layout = None

    def __init__(self):
        self._storage = Storage.Storage()

    def markup(self):
        raise Exception("Markup not found.")

    def add_widgets(self, widgets):
        for i in widgets:
            self.layout.addWidget(i)
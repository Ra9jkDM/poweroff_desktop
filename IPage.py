class IPage:
    layout = None
    _navigator = None

    def markup(self):
        raise Exception("Markup not found.")

    def add_widgets(self, widgets):
        for i in widgets:
            self.layout.addWidget(i)
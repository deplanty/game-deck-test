from src.tui import Widget


class Frame(Widget):
    """
    A simple widget use to contains other widgets

    Args:
        parent (Widget): The parent widget
    """

    def __init__(self, parent):
        super().__init__(parent)

    def update(self):
        pass

from src.tui import Widget
from src.tui.style import Style, BoxClean


class HLine(Widget):
    """
    A simple widget that displays an horizontal line.

    Args:
        parent (Widget): The parent widget.
        style: The style used to show this label.
    """

    def __init__(self, parent:Widget, style=Style.NORMAL):
        super().__init__(parent)
        self.style = style

    # Methods

    def update(self):
        line = BoxClean.H * self.width
        self.addstr(self.y, self.x, line)

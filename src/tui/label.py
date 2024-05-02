import textwrap

from src.tui import Widget


class Label(Widget):
    """
    A simple widget that displays some text.

    Args:
        parent (Widget): The parent widget
    """

    def __init__(self, parent, text:str=""):
        super().__init__(parent)
        self._text = text

    # Properties

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value:str):
        self._text = value

    # Methods

    def update(self):
        x = self.parent.grid_get_column_position(self.column)
        y = self.parent.grid_get_row_position(self.row)
        width = self.parent.grid_get_column_width(self.column)
        height = self.height

        text = textwrap.wrap(self._text, width)
        nlines = min(height, len(text))
        for i in range(nlines):
            self.main.scr.addstr(y + i, x, text[i])

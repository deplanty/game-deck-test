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
        x = self.x
        y = self.y
        width = self.width
        height = self.height

        print(x, y, width, height)

        text = textwrap.wrap(self._text, width)
        nlines = min(height, len(text))
        for i in range(nlines):
            self.main.scr.addstr(y + i, x, text[i])

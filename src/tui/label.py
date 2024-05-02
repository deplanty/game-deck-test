import textwrap

from src.tui import Widget


class Label(Widget):
    """
    A simple widget that displays some text.

    Args:
        parent (Widget): The parent widget
    """

    def __init__(self, parent, text:str="", align="left"):
        super().__init__(parent)
        self._text = text
        self.align = align

    # Properties

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value:str):
        self._text = str(value)

    @property
    def align(self) -> str:
        return self._align

    @align.setter
    def align(self, value:str):
        """One in [left, center, right]."""

        _valid = ["left", "center", "right"]
        if value not in _valid:
            raise ValueError(f"{value} not in {_valid}")
        self._align = value

    # Methods

    def update(self):
        x = self.x
        y = self.y
        width = self.width
        height = self.height

        text = textwrap.wrap(self._text, width)
        nlines = min(height, len(text))
        for i in range(nlines):
            if self.align == "left":
                line = text[i]
            elif self.align == "right":
                line = f"{text[i]:>{width}}"
            elif self.align == "center":
                line = f"{text[i]:^{width}}"
            self.addstr(y + i, x, line)

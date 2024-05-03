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
        # Separate the different lines of the text.
        # Wrap the line that are longer than the frame width.
        # Store each line in a list.
        text_split = self._text.split("\n")
        lines = list()
        for line in text_split:
            text = textwrap.wrap(line, self.width)
            for line in text:
                if self.align == "left":
                    pass
                elif self.align == "right":
                    line = f"{line:>{self.width}}"
                elif self.align == "center":
                    line = f"{line:^{self.width}}"
                lines.append(line)

        # Display as many lines as the frame height allows.
        nlines = min(self.height, len(lines))
        for i in range(nlines):
            self.addstr(self.y + i, self.x, lines[i])

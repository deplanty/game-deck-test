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

        # Flags
        self._flag_fill = False  # Fill the widget with blank to remove previous text.

    # Properties

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value:str):
        self._text = str(value)
        self._flag_fill = True

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
        self._flag_fill = True

    # Methods

    def update(self):
        # If the label is modified, then the flag is up and the widget must be reset.
        if self._flag_fill:
            self.fill(" ")
            self._flag_fill = False

        lines = self._get_text_as_list()
        # Display as many lines as the frame height allows.
        nlines = min(self.height, len(lines))
        for i in range(nlines):
            self.addstr(self.y + i, self.x, lines[i])

    def _get_text_as_list(self) -> list[str]:
        """
        Separate the different lines of the text.
        Wrap the lines that are longer than the widget's width.
        Return each line in a list.

        Returns:
            list[str]: All the lines to display on screen.
        """

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

        return lines

import textwrap

from src.tui import Widget
from src.tui.style import Style


class Label(Widget):
    """
    A simple widget that displays some text.

    Args:
        parent (Widget): The parent widget.
        text (str): The text displayed.
        prefix (str): A text to display right before the main text.
        suffix (str): A text to display right after the main text.
        align (str): How the text is displayed (left, center, right).
        style: The style used to show this label.
        style_filler (bool): Use the style of the label for its whole width.

    Other attributes:
        prefix_always (bool): If True, always show the prefix before the main text.
        suffix_always (bool): If False, hide the suffix after the main text when it is empty.
    """

    def __init__(self, parent:Widget, text:str="", prefix:str="", suffix:str="", align:str="left", style=Style.NORMAL, style_filler:bool=False):
        super().__init__(parent)
        self.text = text
        self.prefix = prefix
        self.suffix = suffix
        self.align = align
        self.style = style

        self._style_filler = style_filler

        # If `prefix_always` is True, it is shown even if the text is empty
        self.prefix_always = True
        # If `suffix_always` is False, it is hidden when the text is empty
        self.suffix_always = False

    # Properties

    @property
    def text(self) -> str:
        """The text of the label.
        
        This text do not include the prefix nor the suffix.
        """

        return self._text

    @text.setter
    def text(self, value:str):
        """Set the text of the label.
        
        When the text is set, the flag that indicates that the widget should be filled to remove
        the previous text is set to True.
        """

        self._text = str(value)
        self._flag_fill = True

    @property
    def prefix(self) -> str:
        """The prefix of the label is displayed right before the text."""

        return self._prefix

    @prefix.setter
    def prefix(self, value:str):
        self._prefix = str(value)
        self._flag_fill = True

    @property
    def suffix(self) -> str:
        """The suffix of the label is displayed right after the text."""

        return self._suffix

    @suffix.setter
    def suffix(self, value:str):
        self._suffix = str(value)
        self._flag_fill = True

    @property
    def align(self) -> str:
        """The alignment of the text in the label: right, left or center."""

        return self._align

    @align.setter
    def align(self, value:str):
        """One in [left, center, right]."""

        _valid = ["left", "center", "right"]
        if value not in _valid:
            raise ValueError(f"{value} not in {_valid}")
        self._align = value
        self._flag_fill = True

    @property
    def text_full(self) -> str:
        """The full text of the label including the prefix and the suffix.

        If the text is empty, only the prefix is shown. For exemple, if the prefix is "Size: " the
        suffix is a unit " cm", the full text will be "Size:  cm" whereas it should be "Size: ".
        """

        if self.text:
            return self.prefix + self.text + self.suffix
        else:
            text = ""
            if self.prefix_always:
                text += self.prefix
            if self.suffix_always:
                text += self.suffix
            return text

    @property
    def height_calc(self) -> int:
        """
        Overwrite the Widget.height_calc property.
        The height of a label is given by the number of lines needed to fully display its content.
        """

        return len(self._get_text_as_list())

    # Methods

    def update(self):
        # If the label is modified, then the flag is up and the widget must be reset.
        if self._flag_fill:
            self.fill(self._style_filler)
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

        text_split = self.text_full.split("\n")
        lines = list()
        for line in text_split:
            text = textwrap.wrap(line, self.width, replace_whitespace=False, drop_whitespace=False)
            for line in text:
                if self.align == "left":
                    pass
                elif self.align == "right":
                    line = f"{line:{self._filler}>{self.width}}"
                elif self.align == "center":
                    line = f"{line:{self._filler}^{self.width}}"
                lines.append(line)

        return lines

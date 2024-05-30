from src.tui import Widget
from src.tui.style import Style


class Progressbar(Widget):
    def __init__(self, parent, maximum:int=100, align:str="left", display:str="value", style:str=Style.NORMAL):
        super().__init__(parent)

        self._maximum = maximum
        self._current = 0
        self.align = align
        self.display = display
        
        self.set_style(style)

    def __add__(self, value:int):
        self._current = min(self._maximum, self._current + value)
        return self

    def __sub__(self, value:int):
        self._current = min(self._maximum, self._current + value)
        return self

    # Properties

    @property
    def percent(self) -> float:
        """Return the percent of progression."""

        return self._current / self._maximum

    @property
    def maximum(self) -> int:
        """The maximum value of this progressbar."""

        return self._maximum

    @maximum.setter
    def maximum(self, value:int):
        self._maximum = int(value)

    @property
    def current(self) -> int:
        """The current value of this progressbar."""

        return self._current

    @current.setter
    def current(self, value:int):
        self._current = int(value)

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

    @property
    def display(self) -> str:
        return self._display

    @display.setter
    def display(self, value:str):
        """One in [value, percent]."""

        _valid = ["none", "value", "percent"]
        if value not in _valid:
            raise ValueError(f"{value} not in {_valid}")
        self._display = value

    # Methods

    def fill(self):
        """End the progression."""

        self._current = self._maximum

    def empty(self):
        """Reset the progression."""

        self._current = 0

    def update(self):
        # Characters used
        fill = "█"
        empty = "▒"
        around = ["[", "]"]

        # How the value is displayed
        if self.display == "value":
            value = f"{self._current}/{self._maximum}"
        elif self.display == "percent":
            value = f"{self.percent * 100:05.1f}%"
        elif self.display == "none":
            value = ""
            around = ["", ""]

        # Display the progression line according to the display method:
        # value + fill + empty
        if self.align == "left":
            value = value + around[1]
            pixel = round((self.width - len(value)) * self.percent)
            line = value
            line += fill * pixel
            line += empty * ((self.width - len(value)) - pixel)
        elif self.align == "center":
            value = around[0] + value + around[1]
            pixel = round(self.width * self.percent)
            line = value.center(pixel, fill)
            line = line.center(self.width, empty)
        elif self.align == "right":
            value = around[0] + value
            pixel = round((self.width - len(value)) * self.percent)
            line = empty * ((self.width - len(value)) - pixel)
            line += fill * pixel
            line += value

        # Display the line on the screen
        self.addstr(self.y, self.x, line)

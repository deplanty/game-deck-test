import curses

from src.tui import Widget
from src.tui.style import BoxClean, Style


class Frame(Widget):
    """
    A simple widget use to contains other widgets

    Args:
        parent (Widget): The parent widget
        border (bool): This frame have borders or not. TODO: WIP
    """

    style_border = BoxClean

    def __init__(self, parent, border:bool=False, border_title:str=""):
        super().__init__(parent)

        self.border = border
        self.border_title = border_title
        if self.border:
            self.pad_intern.x = 1
            self.pad_intern.y = 1

    @property
    def border_title(self) -> str:
        return self._border_title

    @border_title.setter
    def border_title(self, title:str):
        self._border_title = title

    @property
    def height_calc(self) -> int:
        """The height of this widget depends on the height of its children.

        If the widget doesn't have any child, the height is 1 row.
        If the widget have children, the height depends on the layout.
            - For grid: it's the sum of the height of each row.
            - For pack: it's the sum of the height of each child.
            - TODO: For place: ... It's... something? ... WIP !
        """

        if not self.children:
            if self.border:
                return self.pad_intern.y * 2
            else:
                return 1

        layout = self.children[0]._layout
        if layout == "grid":
            rows = dict()
            for child in self.children:
                if child._grid.row not in rows:
                    rows[child._grid.row] = list()
                rows[child._grid.row].append(child)

            height = 0
            for children in rows.values():
                height += max(child.height_calc for child in children)
            return height

        elif layout == "pack":
            h = sum(child.height for child in self.children)
            return self.pad_intern.y * 2 + h
        elif layout == "place":
            return self.pad_intern. y * 2

    def update(self):
        if self.border:
            # The string to display
            line = self.style_border.H * (self.width - 2)
            top = f"{self.style_border.TL}{line}{self.style_border.TR}"
            bottom = f"{self.style_border.BL}{line}{self.style_border.BR}"

            # Display the strings with the correct style
            self.set_style(Style.TEXT_MUTED)
            self.addstr(self.y, self.x, top)
            row = 0
            for row in range(1, self.height - 1):
                self.addstr(self.y + row, self.x, self.style_border.V)
                self.addstr(self.y + row, self.x + self.width - 1, self.style_border.V)
            self.addstr(self.y + row + 1, self.x, bottom)

            self.set_style(Style.NORMAL)
            self.addstr(self.y, self.x + 1, self.border_title)
        else:
            pass

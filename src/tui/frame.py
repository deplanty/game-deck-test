from src.tui import Widget


class Frame(Widget):
    """
    A simple widget use to contains other widgets

    Args:
        parent (Widget): The parent widget
        border (bool): This frame have borders or not. TODO: WIP
    """

    def __init__(self, parent, border:bool=False):
        super().__init__(parent)

        self.border = border
        if self.border:
            self.pad_intern.x = 1
            self.pad_intern.y = 1

    @property
    def height_calc(self) -> int:
        """The height of this widget depends on the height of its children.

        If the widget doesn't have any child, the height is 1 row.
        If the widget have children, the height depends on the layout.
            - For grid: it's the sum of the height of each row.
            - For pack: it's the sum of the height of each child.
            - TODO: For place: ... It's... something? ... WIP !"""

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
            if self.border:
                return self.pad_intern.y * 2 + 4
            else:
                return 1
        elif layout == "place":
            if self.border:
                return self.pad_intern. y * 2
            else:
                return 1

    def update(self):
        if self.border:
            line = "-" * (self.width - 2)
            top = f"+{line}+"
            bottom = f"+{line}+"
            self.addstr(self.y, self.x, top)
            for row in range(1, self.height - 1):
                self.addstr(self.y + row, self.x, "|")
                self.addstr(self.y + row, self.x + self.width - 1, "|")
            self.addstr(self.y + row + 1, self.x, bottom)
        else:
            pass

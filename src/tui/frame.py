from src.tui import Widget


class Frame(Widget):
    """
    A simple widget use to contains other widgets

    Args:
        parent (Widget): The parent widget
    """

    def __init__(self, parent:Widget):
        super().__init__(parent)

    @property
    def height_calc(self) -> int:
        """The height of this widget depends on the height of its children.

        If the widget doesn't have any child, the height is 1 row.
        If the widget have children, the height depends on the layout.
            - For grid: it's the sum of the height of each row.
            - For pack: it's the sum of the height of each child.
            - For place: the height is defined by the layout.
        """

        if not self.children:
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
            return self._place.height

    def update(self):
        if self._flag_fill:
            self.fill()

import curses


class Widget:
    """
    The base class for all widgets.

    Args:
        parent (Widget): The parent widget.
    """

    # The main window widget is accessible from every one here.
    # The tui.Tui class set its value.
    main = None

    def __init__(self, parent):
        self.parent = parent
        self.children = list()

        # Grid position
        self.row = 0
        self.column = 0
        self.row_span = 1
        self.column_span = 1

        # Paramters
        self._filler = " "
        self._flag_fill = False

        # At the end of this instanciation, add this widget as a child
        if parent is not None:
            self.parent.add_child(self)

    def __str__(self) -> str:
        parents = [self.__class__.__name__]
        parent = self.parent
        while parent is not None:
            parents.insert(0, parent.__class__.__name__)
            parent = parent.parent
        return ".".join(parents)

    # Properties

    @property
    def x(self) -> int:
        """Returns the absolute column position of the widget."""

        if self.parent is None:
            return 0
        else:
            return self.parent.x + self.parent.grid_get_column_position(self.column)

    @property
    def y(self) -> int:
        """Returns the absolute row position of the widget."""

        if self.parent is None:
            return 0
        else:
            return self.parent.y + self.parent.grid_get_row_position(self.row)

    @property
    def width(self) -> int:
        """Returns the width of the widget."""

        if self.parent is None:
            return curses.COLS
        else:
            return self.parent.grid_get_column_width(self.column)

    @property
    def height(self) -> int:
        """Returns the height of the widget."""

        if self.parent is None:
            return curses.LINES
        else:
            return self.parent.grid_get_row_height(self.row) * self.row_span

    @property
    def filler(self) -> str:
        return self._filler

    @filler.setter
    def filler(self, char:str):
        if len(char) != 1:
            raise ValueError(f"String '{char}' was given but only one char was expected")
        self._filler = char
        self._flag_fill = True

    @property
    def grid_nrows(self) -> int:
        """The number of rows in the grid of this widget."""

        rows = max(0, *(child.row for child in self.children))
        return rows + 1

    @property
    def grid_ncolumns(self) -> int:
        """The number of columns in the grid of this widget."""

        columns = max(0, *(child.column for child in self.children))
        return columns + 1

    # Methods

    def update(self):
        """How the widget displays information."""

        raise NotImplementedError()

    def _update(self):
        """Hiden function to update all the children widgets and this widget."""

        for child in self.children:
            child.update()
            child._update()
        self.update()

    def add_child(self, child):
        """
        Add a child to this widget

        Args:
            child (Widget): The child widget.
        """

        self.children.append(child)
        self.children.sort(key=lambda x: x.row)

    def grid(self, row:int, column:int=0, row_span:int=1, column_span:int=1):
        """
        How should be displayed the widget with its siblings.
        FIXME: Manage when several widgets are on the same "grid cell".

        Args:
            row (int): The grid row.
            column (int): The grid column. Defaults to 0.
            row_span (int): The number of grid row this widget takes.
            column_span (int): The number of grid column this widget takes.
        """

        self.row = row
        self.column = column
        self.row_span = row_span
        self.column_span = column_span

    def grid_get_row_position(self, row:int) -> int:
        """
        Returns the relative row position of a child (given from its grid row).

        Args:
            row (int): The grid row.

        Returns:
            int: The absolute position.
        """

        row_position = 0
        for i in range(row):
            row_position += self.grid_get_row_height(i)
        return row_position

    def grid_get_row_height(self, row:int) -> int:
        """
        Returns the height of a row in the grid.
        TODO: Use self.row_span.

        Args:
            row (int): The grid row.

        Returns:
            int: The height of the row.
        """

        rows = max(child.row + child.row_span - 1 for child in self.children) + 1
        height = self.height // rows
        return height

    def grid_get_column_position(self, column:int) -> int:
        """
        Returns the relative column position of a child (given from its grid column).

        Args:
            column (int): The grid column.

        Returns:
            int: The absolute position
        """

        col_position = 0
        for i in range(column):
            col_position += self.grid_get_column_width(i)
        return col_position

    def grid_get_column_width(self, column:int) -> int:
        """
        Returns the width of a column in the grid.

        Args:
            column: The grid column.

        Returns:
            int: The width of the column.
        """

        columns = max(child.column for child in self.children) + 1
        width = self.width // columns
        return width

    def addstr(self, y:int, x:int, text:str, *args, **kwargs):
        self.main.scr.addstr(y, x, text, *args, *kwargs)

    def fill(self):
        """Fill the widget with the char `self.filler`."""

        line = self.filler * self.width
        for row in range(self.height):
            self.addstr(self.y + row, self.x, line)

    def focus_set(self):
        self.main.focus_widget = self

    def focus(self):
        self.main.scr.move(self.y, self.x)
        self.main.focus_widget._on_focus()

    def _on_focus(self):
        pass

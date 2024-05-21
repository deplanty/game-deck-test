import curses


class Grid:
    def __init__(self, row:int=0, column:int=0, rowspan:int=1, columnspan:int=1):
        self.row = row
        self.column = column
        self.rowspan = rowspan
        self.columnspan = columnspan


class Place:
    def __init__(self, x:int=0, y:int=0, width:int=1, height:int=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


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

        self.focus_next = None

        # How to position the widget
        self._grid = Grid()
        self._place = Place()  # TODO: place the widget at a particular position and size

        # Paramters
        self.filler = " "
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
            return self.parent.x + self.parent.grid_get_column_position(self._grid.column)

    @property
    def y(self) -> int:
        """Returns the absolute row position of the widget."""

        if self.parent is None:
            return 0
        else:
            return self.parent.y + self.parent.grid_get_row_position(self._grid.row)

    @property
    def width(self) -> int:
        """Returns the width of the widget."""

        if self.parent is None:
            return curses.COLS
        else:
            return self.parent.grid_get_column_width(self._grid.column) * self._grid.columnspan

    @property
    def height(self) -> int:
        """Returns the height of the widget."""

        if self.parent is None:
            return curses.LINES
        else:
            return self.parent.grid_get_row_height(self._grid.row) * self._grid.rowspan

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
    def focus_next(self) -> "Widget":
        return self._focus_next

    @focus_next.setter
    def focus_next(self, widget:"Widget"):
        self._focus_next = widget

    # Methods

    def update(self):
        """How the widget displays information."""

        raise NotImplementedError()

    def _update(self):
        """Hiden function to update all the children widgets and this widget."""

        for child in self.children:
            child._update()
        self.update()

    def add_child(self, child):
        """
        Add a child to this widget

        Args:
            child (Widget): The child widget.
        """

        self.children.append(child)
        self.children.sort(key=lambda x: x._grid.row)

    def grid(self, row:int, column:int=0, rowspan:int=1, columnspan:int=1):
        """
        How should be displayed the widget with its siblings.

        Args:
            row (int): The grid row.
            column (int): The grid column. Defaults to 0.
            rowspan (int): The number of grid row this widget takes.
            columnspan (int): The number of grid column this widget takes.
        """

        self._grid.row = row
        self._grid.column = column
        self._grid.rowspan = rowspan
        self._grid.columnspan = columnspan

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
        TODO: Use self.rowspan.

        Args:
            row (int): The grid row.

        Returns:
            int: The height of the row.
        """

        rows = max(child._grid.row + child._grid.rowspan - 1 for child in self.children) + 1
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

        columns = max(child._grid.column + child._grid.columnspan - 1 for child in self.children) + 1
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

    def focus_remove(self):
        if self.main.focus_widget == self:
            self.main.focus_widget = None

    def focus(self) -> str:
        """
        When a widget have the focus, set the cursor at its position and execute its function.

        Returns:
            str: The status of the output.
        """

        self.main.scr.move(self.y, self.x)
        return self._on_focus()

    def _on_focus(self):
        pass

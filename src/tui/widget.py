import copy
import curses

from src.tui.style import Style

from .layout import Grid, Pack, Place


class Vector2:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y


class Widget:
    """
    The base class for all widgets.

    Args:
        parent (Widget): The parent widget.
    """

    # The main window widget is accessible from every one here.
    # The tui.Tui class set its value.
    main = None

    def __init__(self, parent:"Widget"):
        self.parent = parent
        self.children = list()

        self.pad_intern = Vector2(0, 0)

        # Focus
        self.focus_next = None
        self._is_on_focus = False  # If the widget is currently focused

        # How to position the widget
        self._layout = ""  # How the widget is placed in its parent
        self._grid = Grid()
        self._place = Place()
        self._pack = Pack()

        # Visibility of the widget
        self._visible = True

        # Fill the widget to hide previous characters
        self.filler = " "
        self._flag_fill = False

        # Style
        self.style = Style.NORMAL

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

        # dx is the position of the widget according to its parent
        dx = 0
        if self._layout == "grid":
            dx = self.parent._grid_get_column_position(self._grid.column)
        elif self._layout == "pack":
            dx = 0
        elif self._layout == "place":
            # The x position can be absolute or relative
            if self._place.is_x_abs():
                dx = self._place.x
            else:
                dx = round(self.parent.width * self._place.x)

            if self._place.anchor == "center":
                dx -= round(self.width / 2)

        return self.parent.x + self.parent.pad_intern.x + dx

    @property
    def y(self) -> int:
        """Returns the absolute row position of the widget."""

        if self.parent is None:
            return 0

        # dy is the position of the widget according to its parent
        dy = 0
        if self._layout == "grid":
            dy = self.parent._grid_get_row_position(self._grid.row)
        elif self._layout == "pack":
            dy = self.parent._pack_get_row_position(self)
        elif self._layout == "place":
            # The y position can be absolute or relative
            if self._place.is_y_abs():
                dy = self._place.y
            else:
                dy = round(self.parent.height * self._place.y)

            if self._place.anchor == "center":
                dy -= round(self.height / 2)

        return self.parent.y + self.parent.pad_intern.y + dy

    @property
    def width(self) -> int:
        """Returns the width of the widget."""

        if self.parent is None:
            return curses.COLS

        w = 0
        if self._layout == "grid":
            w = self.parent._grid_get_column_width(self._grid.column) * self._grid.columnspan
        elif self._layout == "pack":
            w = self.parent.width
        elif self._layout == "place":
            # The width can be absolute or relative
            if self._place.is_width_abs():
                w = self._place.width
            else:
                w = round(self.parent.width * self._place.width)

        return w - self.parent.pad_intern.x * 2

    @property
    def height(self) -> int:
        """Returns the height of the widget."""

        if self.parent is None:
            return curses.LINES

        h = 0
        if self._layout == "grid":
            h = self.parent._grid_get_row_height(self._grid.row) * self._grid.rowspan
        if self._layout == "pack":
            h = self.parent._pack_get_height(self)
        elif self._layout == "place":
            # The height can be absolute or relative
            if self._place.is_height_abs():
                h = self._place.height
            else:
                h = round(self.parent.height * self._place.height)

        return h

    @property
    def height_calc(self) -> int:
        """The calculated height of a widget.

        The calculated height represents the height taken by the widget to fully show its content.
        The widgets that are containers, such as the Frame, doesn't have a proper height and rely
        on the height of its children.
        The widgets that are elements, such as the Label, have an intrinsect height.
        """

        return 1

    @property
    def visible(self) -> bool:
        """The visibility state of the widget."""

        return self._visible

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

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, style):
        self._style = copy.deepcopy(style)

    # Methods required

    def update(self):
        """How the widget displays information."""

        raise NotImplementedError()

    def _update(self):
        """Hiden function to update all the children widgets and this widget."""

        if self.visible:
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

    # Methods general

    def addstr(self, y:int, x:int, text:str, *args, **kwargs):
        """Write a string. The string cannot overflow the window size."""

        if x + len(text) > curses.COLS:
            end_too_long = "~]"
            allowed = curses.COLS - x - len(end_too_long)
            text = text[:allowed] + end_too_long
        self.main.scr.addstr(y, x, text, self.style.apply(), *args, *kwargs)

    def getch(self) -> str:
        """Wait a char from the user."""

        return self.main.scr.getch()

    def fill(self, use_style=False):
        """Fill the widget with the char `self.filler`."""

        line = self.filler * self.width

        if not use_style:
            style = self.style
            self.style = Style.NORMAL

        for row in range(self.height):
            self.addstr(self.y + row, self.x, line)

        if not use_style:
            self.style = style

    def show(self):
        """If the widget was hidden, show it."""

        self._visible = True

    def hide(self):
        """If the widget was visible, hide it."""

        self._visible = False

    # Methods for layout

    def grid(self, row:int, column:int=0, rowspan:int=1, columnspan:int=1):
        """
        The widget is displayed if a grid.

        Args:
            row (int): The grid row.
            column (int): The grid column. Defaults to 0.
            rowspan (int): The number of grid row this widget takes.
            columnspan (int): The number of grid column this widget takes.
        """

        layouts = self._get_layout_siblings()
        if any(l != "grid" for l in layouts if l):
            raise Exception(f"Can't use layout 'grid' with '{layouts[0]}' already in use")

        self._layout = "grid"
        self._grid.set(row, column, rowspan, columnspan)

    def pack(self, fill:bool=False):
        """
        The widget are packed one above the other.
        """

        layouts = self._get_layout_siblings()
        if any(l != "pack" for l in layouts if l):
            raise Exception(f"Can't use layout 'pack' with '{layouts[0]}' already in use")

        self._layout = "pack"
        self._pack.set(fill)

    def place(self, x:int|float=None, y:int|float=None, width:int|float=1, height:int|float=1,
              anchor:str="nw"):
        """
        The widget is placed at a given position.

            Args:
                x (int|float): The x (column) position (int=absolute, float=relative).
                y (int|float): The y (row) position (int=absolute, float=relative).
                width (int|float): The width allowed (int=absolute, float=relative).
                height (int|float): The height allowed (int=absolute, float=relative).
                anchor (str): Where the widget is anchored (normal, center).
        """

        self._layout = "place"
        self._place.set(x, y, width, height, anchor)

    def _grid_get_row_position(self, row:int) -> int:
        """
        Returns the relative row position of a child (given from its grid row).

        Args:
            row (int): The grid row.

        Returns:
            int: The absolute position.
        """

        row_position = 0
        for i in range(row):
            row_position += self._grid_get_row_height(i)
        return row_position

    def _grid_get_row_height(self, row:int) -> int:
        """
        Returns the height of a row in the grid.

        Args:
            row (int): The grid row.

        Returns:
            int: The height of the row.
        """

        rows = max(child._grid.row + child._grid.rowspan - 1 for child in self.children) + 1
        height = self.height // rows
        return height

    def _grid_get_column_position(self, column:int) -> int:
        """
        Returns the relative column position of a child (given from its grid column).

        Args:
            column (int): The grid column.

        Returns:
            int: The relative position
        """

        col_position = 0
        for i in range(column):
            col_position += self._grid_get_column_width(i)
        return col_position

    def _grid_get_column_width(self, column:int) -> int:
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

    def _pack_get_row_position(self, widget) -> int:
        """
        Returns the relative row position of a child widget.

        Args:
            widget (Widget): The child widget.

        Returns:
            int: The relative row position in this widget.
        """

        row = 0
        for child in self.children:
            if child == widget:
                return row
            row += self._pack_get_height(child)

    def _pack_get_height(self, widget) -> int:
        """Returns the height of a child packed widget.

        If the widget is simply packed (without fill), its height is height_calc.
        If the widget is packed with fill (= y fill), its height is calculated by self (its parent).
        """

        if not widget._pack.fill:
            return widget.height_calc
        else:
            # Get how many children are packed with fill and get the height of the others
            fill_n = 0
            height_other = 0
            for child in self.children:
                if child._pack.fill:
                    fill_n += 1
                else:
                    height_other += child.height_calc
            # The height of this widget is the remaining height shared with the other filled.abs
            h = (self.height - height_other) // fill_n
            if fill_n == 1:
                h -= 1
            recalc = height_other + h * fill_n
            if recalc >= self.height:
                h -= 1
            return h

    def _get_layout_siblings(self) -> list[str]:
        """Return a list with the layout of all the siblings"""

        return [child._layout for child in self.parent.children]

    def focus_set(self):
        """Set this widget as the current focused widget."""

        self.main.focus_widget = self

    def focus_remove(self):
        if self.main.focus_widget == self:
            self.main.focus_widget = None

    def _focus_run(self) -> str:
        """
        When a widget have the focus, set the cursor at its position and execute its function.

        Returns:
            str: The status of the output.
        """

        self.main.scr.move(self.y, self.x)
        self._is_on_focus = True
        result = self._on_focus()
        self._is_on_focus = False
        return result

    def _on_focus(self):
        """Placeholder for subsequent inherited Widget that can be focused."""

        pass

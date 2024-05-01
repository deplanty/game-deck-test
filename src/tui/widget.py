class Widget:
    """
    The base class for all widgets.

    Args:
        parent (Widget): The parent widget.
    """

    def __init__(self, parent):
        self.parent = parent
        self.children = list()

        # Grid position and size
        self.row = 0
        self.column = 0
        self.height = 1

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
    def pos_row(self) -> int:
        """Returns the top row position of the widget."""

        if self.parent is None:
            return 0
        else:
            return self.parent.pos_row + self.row

    @property
    def pos_column(self) -> int:
        """Returns the left column position of the widget."""
        if self.parent is None:
            return 0
        else:
            return self.parent.pos_column + self.column

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

    def grid(self, row:int, column:int=0, height:int=1):
        """
        How should be displayed the widget with its siblings.

        Args:
            row (int): The grid row
            column (int): The grid column. Defaults to 0.
            height (int): The height of the widget. Defaults to 1.

        FIXME: Manage when several widgets are on the same "grid cell".
        """

        self.row = row
        self.column = column
        self.height = height

    def grid_get_row_position(self, row:int) -> int:
        """
        Returns the absolute row position for ont of its child from a griven
        grid row.

        Args:
            row (int): The grid row.

        Returns:
            int: The absolute position.
        """

        row_position = self.pos_row
        for i in range(row):
            row_position += self.children[i].height
        return row_position

import curses

from src import tui
from src.tui import Signal
from src.tui.style import Style
from src.tui.keys import Keys
from src.utils import GridIndex


class ChoiceWidget(tui.Widget):

    hovered:Signal
    selected:Signal

    def __init__(self, parent:tui.Widget, prefix:str="", columns:int=1):
        super().__init__(parent)

        self.prefix = prefix
        self.columns = columns

        self.selected = Signal()
        self.hovered = Signal()

        if self.prefix:
            self.label_prefix = tui.Label(self, text=self.prefix)
            self.label_prefix.pack()
        self.frame = tui.Frame(self)
        self.frame.pack()

        self.position = GridIndex(columns=columns)
        self._selected = -1

    @property
    def height_calc(self) -> int:
        n_rows, _ = self._index_to_grid(len(self.frame.children))

        h = self.label_prefix.height_calc
        grid = self.frame._grid_get_row_height(0) * n_rows

        return h + grid

    @property
    def children_choice(self) -> str:
        return self.frame.children

    # Events

    def _on_focus(self) -> str:
        """
        This function is triggered when a widget gets the focus.

        Returns:
            str: The choice made.
        """

        self.hovered.emit()
        curses.cbreak()
        # Cursor size:
        #   - 0 invisible
        #   - 1 small (bar)
        #   - 2 big (block)
        cursor_previous = curses.curs_set(0)

        state = ""
        while state == "":
            self.update()
            key = self.getch()
            if key == Keys.ARROW_UP:
                self.position.row -=1
                self.hovered.emit()
            elif key == Keys.ARROW_DOWN:
                self.position.row += 1
                self.hovered.emit()
            elif key == Keys.ARROW_LEFT:
                self.position.column -= 1
                self.hovered.emit()
            elif key == Keys.ARROW_RIGHT:
                self.position.column += 1
                self.hovered.emit()
            elif key == Keys.RETURN:
                self._selected = self.position.index
                self.selected.emit()
                state = "ok"
            elif key == Keys.TABLUATION:
                state = "tab"
            elif key == Keys.TABLUATION_BACK:
                state = "tab_back"
            elif key == Keys.ESCAPE:
                self._selected = -1

        curses.nocbreak()
        curses.curs_set(cursor_previous)

        return state

    # Methods Required

    def update(self):
        # 3 possible states for the selector:
        #   - Selected: show the selector
        #   - Not selected and not current: show the selector_empty
        #   - Not selected and current: show the selecter_tmp
        for i, widget in enumerate(self.children_choice):
            # FIXME: not all widget have a style_border attribute. Only LabelFrame.
            if self._selected == i:
                widget.style_border = Style.TEXT_SECONDARY
            elif self._is_on_focus and self.position.index == i:
                widget.style_border = Style.TEXT_PRIMARY
            else:
                widget.style_border = Style.MUTE
            widget.update()

    # Methods

    def add_widget(self, widget:tui.Widget, *args, **kwargs):
        """Add a widget as a selectable option."""

        row, col = self._index_to_grid(len(self.frame.children))
        w = widget(self.frame, *args, **kwargs)
        w.grid(row, col)

        self.position.total += 1

    def reset(self):
        """Reset all the data in the widget"""

        self.frame.children.clear()

        self.position.index = 0
        self.position.total = 0
        self._selected = -1

    def select(self, index:int):
        """
        Select the given item by its index.

        Args:
            index (int): Index of the item to select.
        """

        self._selected = index
        self.selected.emit()

    def _index_to_grid(self, index:int) -> tuple[int]:
        row, col = divmod(index, self.columns)
        return row, col

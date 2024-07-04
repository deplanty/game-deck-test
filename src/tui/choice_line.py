import curses

from src import tui
from src.tui import Widget, Signal
from src.tui.keys import Keys


class ChoiceLine(Widget):

    hovered:Signal
    selected:Signal

    def __init__(self, parent:Widget, prefix:str="", selector:str=">>", selector_empty:str="  ", selector_tmp:str="> "):
        super().__init__(parent)

        self.prefix = prefix
        self.selector = selector
        self.selector_empty = selector_empty
        self.selector_tmp = selector_tmp

        self.choices = list()

        self.selected = Signal()
        self.hovered = Signal()

        self.current = 0  # Current selection
        self._selected = -1

        if self.prefix:
            self.label_prefix = tui.Label(self, text=self.prefix)
            self.label_prefix.grid(0, 0)

    @property
    def height_calc(self) -> int:
        return max(child.height_calc for child in self.children)

    @property
    def current(self) -> int:
        """Current position of the cursor."""

        return self._current

    @current.setter
    def current(self, value) -> int:
        """Set the position of the cursor.

        It can't be lower than 0 and greater than the number of choices.
        """

        if value >= 0 and (value < len(self.choices) or len(self.choices) == 0):
            self._current = value

    @property
    def choice(self) -> str:
        """
        Return the selected choice as text.
        If nothing was selected, return an empty string.
        """

        return self.choices[self.current] if self._selected != -1 else ""

    @property
    def choice_current(self) -> str:
        """Return the current choice as text."""

        return self.choices[self.current]

    @property
    def children_choice(self) -> str:

        if self.prefix:
            return self.children[1:]
        else:
            return self.children

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
        cursor_previous = curses.curs_set(1)

        state = ""
        while state == "":
            self.update()
            key = self.getch()
            if key == Keys.ARROW_LEFT:
                self.current -= 1
                self.hovered.emit()
            elif key == Keys.ARROW_RIGHT:
                self.current += 1
                self.hovered.emit()
            elif key == Keys.RETURN:
                self._selected = self.current
                self.selected.emit()
                state = "ok"
            elif key == Keys.TABLUATION:
                if self._selected != -1:
                    self.current = self._selected
                state = "tab"
            elif key == Keys.TABLUATION_BACK:
                if self._selected != -1:
                    self.current = self._selected
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
        for i, label in enumerate(self.children_choice):
            # Highlight only the currently selected item
            label.style.reset_modifiers()
            if self._is_on_focus and self.current == i:
                    label.style.bold()

            # Show the correct selector
            if self._selected == i:
                label.prefix = f"{self.selector} "
            elif self._is_on_focus and self.current == i:
                label.prefix = f"{self.selector_tmp} "
            else:
                label.prefix = f"{self.selector_empty} "
            label.text = self.choices[i]
            label.update()
        self._set_cursor_current()

    # Methods

    def add_label(self, text:str, **kwargs):
        """Add a label from text that can be chosen.

        Args:
            text: Text to display in a Label.
            kwargs: Label args.
        """

        self.choices.append(text)
        label = tui.Label(self, text, **kwargs)
        label.grid(0, len(self.children) - 1)

    def add_labels(self, *texts):
        """Add several labels."""

        for text in texts:
            self.add_label(text)

    def add_widget(self, widget:Widget):
        """TODO: Add a widget as a selectable option."""

        raise NotImplementedError()

    def reset_choices(self):
        """Reset all the data in the widget"""

        self.choices.clear()

        # The prefix label is in the children and should be kept
        if self.prefix:
            prefix = self.children.pop(0)
        self.children.clear()
        if self.prefix:
            self.children.append(prefix)

        self.current = 0
        self._selected = -1

    def select(self, index:int):
        """
        Select the given item by its index.

        Args:
            index (int): Index of the item to select.
        """

        self._selected = index
        self.current = index
        self.selected.emit()

    def select_item(self, item):
        """
        Select the given str(item) in the choice.

        Args:
            item (Any): The item that should be selected.
        """

        index = self.choices.index(str(item))
        self.select(index)

    def _set_cursor_current(self):
        """Set the cursor at the current selected line."""

        width = self.label_prefix.width if self.prefix else 0
        for i in range(self.current):
            width += self.children_choice[i].width
        self.main.scr.move(self.y, self.x + width)

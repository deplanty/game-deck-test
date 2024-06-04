import curses

from src import tui
from src.tui import Widget, Signal
from src.tui.keys import Keys


class Choice(Widget):

    hovered:Signal
    selected:Signal

    def __init__(self, parent:Widget, selector:str=">"):
        super().__init__(parent)

        self.selector = selector

        self.choices = list()

        self.selected = Signal()
        self.hovered = Signal()

        self._current = 0  # Current selection
        self._selected = False  # If the Return key has been pressed

    @property
    def height_calc(self) -> int:
        return len(self.choices)

    @property
    def current(self) -> int:
        return self._current

    @current.setter
    def current(self, value) -> int:
        if value >= 0 and value < len(self.choices):
            self._current = value

    @property
    def choice(self) -> str:
        """
        Return the selected choice as text.
        If nothing was selected, return an empty string.
        """

        return self.choices[self.current] if self._selected else ""

    # Events

    def _on_focus(self) -> str:
        """
        This function is triggered when a widget gets the focus.

        Returns:
            str: The choice made.
        """

        self.hovered.emit()
        self._selected = False
        curses.cbreak()
        cursor_previous = curses.curs_set(2)  # Very visible

        state = ""
        while state == "":
            self.update()
            key = self.getch()
            if key == Keys.ARROW_UP:
                self.current -= 1
                self.hovered.emit()
            elif key == Keys.ARROW_DOWN:
                self.current += 1
                self.hovered.emit()
            elif key == Keys.RETURN:
                self._selected = True
                self.selected.emit()
                state = "tab"
            elif key == Keys.TABLUATION:
                self.selected.emit()
                state = "tab"
            elif key == Keys.TABLUATION_BACK:
                state = "tab_back"

        curses.nocbreak()
        curses.curs_set(cursor_previous)

        return state

    # Methods Required

    def update(self):
        for i, label in enumerate(self.children):
            if (self._is_on_focus or self._selected) and self.current == i:
                label.prefix = f"{self.selector} "
            else:
                label.prefix = " " * (len(self.selector) + 1)
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
        label.pack()

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
        self.children.clear()
        self.current = 0
        self._selected = False

    def _set_cursor_current(self):
        """Set the cursor at the current selected line."""

        height = 0
        for i in range(self.current):
            height += self.children[i].height
        self.main.scr.move(self.y + height, self.x)

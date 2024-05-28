import curses

from src import tui
from src.tui.keys import Keys


class Choice(tui.Widget):
    def __init__(self, parent:tui.Widget, selector:str=">"):
        super().__init__(parent)

        self.selector = selector

        self.choices = list()
        self.ui_elements = list()
        self._current = 0

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
        return self.choices[self.current]

    # Events

    def _on_focus(self) -> str:
        """
        This function is triggered when a widget gets the focus.

        Returns:
            str: The choice made.
        """

        curses.cbreak()
        cursor_previous = curses.curs_set(2)  # Very visible
        while True:
            self.update()
            key = self.getch()
            if key == Keys.ARROW_UP:
                self.current -= 1
            elif key == Keys.ARROW_DOWN:
                self.current += 1
            elif key == Keys.RETURN:
                result = "ok"
                break
            elif key == Keys.TABLUATION:
                result = "tab"
                break

        curses.nocbreak()
        curses.curs_set(cursor_previous)

        return result

    # Methods Required

    def update(self):
        for i, label in enumerate(self.ui_elements):
            if self.current == i:
                prefix = f"{self.selector}"
            else:
                prefix = " " * len(self.selector)
            label.text = f"{prefix} {self.choices[i]}"
            label.update()
        self._set_cursor_current()

    # Methods

    def add_element(self, text:str):
        """Add an element that can bee chosen."""

        self.choices.append(text)
        label = tui.Label(self, text)
        label.pack()
        self.ui_elements.append(label)
        
    def add_elements(self, *texts):
        """Add several elements."""

        for text in texts:
            self.add_element(text)
        
    def _set_cursor_current(self):
        """Set the cursor at the current selected line."""

        self.main.scr.move(self.y + self.current, self.x)

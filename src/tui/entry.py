import curses

from src.tui import Widget, Signal
from src.tui.keys import Keys


class Entry(Widget):
    """
    Create an Entry Widget (= TextEdit).

    Args:
        parent (Widget): The parent widget.
        placeholder (str): The string that is displayed when nothing is typed.

    Events:
        keyboard characters: Display them in the widget.
        backspace: Remove the last character.
        escape: Reset the text to its origin.
        return: Validate the entry and stop the internal loop.
        tabulation: Go to next widget in the focus list.
    """

    changed:Signal

    def __init__(self, parent:Widget, placeholder:str="Entry"):
        super().__init__(parent)

        self.placeholder = placeholder
        self.text = ""

        self.changed = Signal()

        self._empty = "░"
        self._cursor = 0

    # Properties

    @property
    def _cursor(self) -> int:
        """Return the current position of the cursor."""

        return self.__cursor

    @_cursor.setter
    def _cursor(self, value:int):
        """Set the position of the cursor.

        The cursor can't be lower than 0 and greater that the size of the text.
        """

        if value < 0:
            self.__cursor = 0
        elif value > len(self.text):
            self.__cursor = len(self.text)
        else:
            self.__cursor = value

    def update(self):
        if self.text == "":
            text = self.placeholder
        else:
            text = self.text

        line = f"{text:{self._empty}<{self.width}}"
        self.addstr(self.y, self.x, line)
        self._place_cursor()

    def _on_focus(self) -> str:
        """
        This function is triggered when a widget gets the focus.

        Returns:
            result: A string representing the output result.
        """

        tmp = self.text
        self._set_cursor_end()
        curses.cbreak()

        state = ""
        while state == "":
            self.update()
            key = self.getch()
            char = chr(key)
            if key == Keys.BACKSPACE:
                self._remove_char()
                self.changed.emit()
            elif key == Keys.TABLUATION:
                state = "tab"
            elif key == Keys.TABLUATION_BACK:
                state = "tab_back"
            elif key == Keys.RETURN:
                state = "ok"
            elif key == Keys.ESCAPE:
                self.text = tmp
                self._set_cursor_end()
                self.changed.emit()
            elif key == Keys.ARROW_LEFT:
                self._cursor -= 1
            elif key == Keys.ARROW_RIGHT:
                self._cursor += 1
            elif char.isprintable():
                self._insert_char(char)
                self.changed.emit()

        curses.nocbreak()

        return state

    def _insert_char(self, char:str):
        """Insert a char at the current cursor position."""
        
        self.text = self.text[:self._cursor] + char + self.text[self._cursor:]
        self._cursor += 1

    def _remove_char(self):
        """Remove a char from the current cursor position."""

        if self._cursor == 0:
            return

        self.text = self.text[:self._cursor - 1] + self.text[self._cursor:]
        self._cursor -= 1

    def _place_cursor(self):
        """Place the cursor on screen at its current position."""

        self.main.scr.move(self.y, self.x + self._cursor)

    def _set_cursor_end(self):
        """Set the cursor at the end of the entry."""

        self._cursor = len(self.text)


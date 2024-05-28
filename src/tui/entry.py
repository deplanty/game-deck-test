import curses

from src.tui import Widget
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

    def __init__(self, parent:Widget, placeholder:str="Entry"):
        super().__init__(parent)

        self.placeholder = placeholder
        self.text = ""

        self._empty = "░"

    def update(self):
        if self.text == "":
            text = self.placeholder
        else:
            text = self.text

        line = f"{text:{self._empty}<{self.width}}"
        self.addstr(self.y, self.x, line)
        self._set_cursor_end()

    def _set_cursor_end(self) -> None:
        self.main.scr.move(self.y, self.x + len(self.text))

    def _on_focus(self) -> str:
        """
        This function is triggered when a widget gets the focus.

        Returns:
            result: A string representing the output result.
        """

        tmp = self.text
        result = "ok"  # FIXME: Do something with this?
        self._set_cursor_end()

        curses.cbreak()
        while True:
            key = self.main.scr.getch()
            char = chr(key)
            if char.isprintable():
                self.text += char
            elif key == Keys.BACKSPACE:
                self.text = self.text[:-1]
            elif key == Keys.TABLUATION:
                result = "tab"
                break
            elif key == Keys.RETURN:
                result = "ok"
                break
            elif key == Keys.ESCAPE:
                self.text = tmp
            self.update()
        curses.nocbreak()

        return result

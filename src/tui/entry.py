import curses

from src.tui import Widget


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

        self._empty = "_"

    def update(self):
        if self.text == "":
            text = self.placeholder
        else:
            text = self.text

        line = f"{text:{self._empty}<{self.width}}"
        self.addstr(self.y, self.x, line)
        self.main.scr.move(self.y, self.x + len(self.text))

    def _on_focus(self) -> str:
        """
        This function is triggered when a widget gets the focus.

        Returns:
            result: A string representing the output result.
        """

        K_BACKSPACE = 8
        K_TABULATION = 9
        K_RETURN = 10
        K_ESCAPE = 27

        tmp = self.text
        result = "ok"  # FIXME: Do something with this?

        curses.cbreak()
        while True:
            key = self.main.scr.getch()
            char = chr(key)
            if char.isprintable():
                self.text += char
            elif key == K_BACKSPACE:
                self.text = self.text[:-1]
            elif key == K_TABULATION:
                result = "tab"
                break
            elif key == K_RETURN:
                result = "ok"
                break
            elif key == K_ESCAPE:
                self.text = tmp
            self.update()
        curses.nocbreak()

        return result

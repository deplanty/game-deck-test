import curses

from src.tui import Widget


class Entry(Widget):
    def __init__(self, parent:Widget, placeholder:str="Entry"):
        super().__init__(parent)

        self.placeholder = placeholder
        self.text = ""

        self._empty = "▁"

    def update(self):
        if self.text == "":
            text = self.placeholder
        else:
            text = self.text

        line = f"{text:{self._empty}<{self.width}}"
        self.addstr(self.y, self.x, line)
        self.main.scr.move(self.y, self.x + len(self.text))

    def _on_focus(self):
        K_BACKSPACE = 8
        K_RETURN = 10
        K_ESCAPE = 27

        tmp = self.text

        curses.cbreak()
        while True:
            key = self.main.scr.getch()
            char = chr(key)
            if char.isprintable():
                self.text += char
            elif key == K_BACKSPACE:
                self.text = self.text[:-1]
            elif key == K_ESCAPE:
                self.text = tmp
                break
            elif key == K_RETURN:
                break
            self.update()
        curses.nocbreak()

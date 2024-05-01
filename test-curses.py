import textwrap

import curses


class Rect:
    def __init__(self, x:int=0, y:int=0, widht:int=0, height:int=0):
        self.x = x
        self.y = y
        self.w = widht
        self.h = height

    def __str__(self) -> str:
        return f"Rect({self.x}, {self.y}, {self.w}, {self.h})"

    def __repr__(self) -> str:
        return str(self)

    # Properties

    @property
    def y_max(self) -> int:
        return self.y + self.h - 1

    @property
    def x_max(self) -> int:
        return self.x + self.w - 1


class Widget:
    def __init__(self, parent, rect:Rect, pair:int=1):
        self.parent = parent
        self.rect = rect
        self.pair = pair

    def fill(self, char:str=" "):
        line = char * self.rect.w
        for row in range(self.rect.h):
            self.parent.addstr(self.rect.y + row, self.rect.x, line, curses.color_pair(self.pair))

    def addstr(self, y:int, x:int, string:str):
        self.parent.addstr(y, x, string, curses.color_pair(self.pair))


class Frame(Widget):
    def __init__(self, parent, rect:Rect, pair:int=1):
        super().__init__(parent, rect, pair)

    def border(self):
        self.fill()
        hline = "+" + "-" * (self.rect.w - 2) + "+"
        self.addstr(self.rect.y, self.rect.x, hline)
        for row in range(self.rect.y + 1, self.rect.y_max):
            self.addstr(row, self.rect.x, "|")
            self.addstr(row, self.rect.x_max, "|")
        self.addstr(self.rect.y_max, self.rect.x, hline)


class Label(Widget):
    # FIXME: How to manage text overflow?
    def __init__(self, parent, rect:Rect, pair:int=1, text:str=""):
        super().__init__(parent, rect, pair)
        self._text = text

    # Properties

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value:str):
        self._text = value
        self.fill()

        text = textwrap.wrap(self._text, self.rect.w)
        nlines = min(self.rect.h, len(text))
        for i in range(nlines):
            self.addstr(self.rect.y + i, self.rect.x, text[i])



def main():
    scr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)
    widget = Frame(scr, Rect(0, 0, 30, 10), 2)
    widget.fill()
    frame = Frame(scr, Rect(0, 11, 30, 10), 3)
    frame.border()
    frame = Frame(scr, Rect(32, 11, 30, 10), 4)
    frame.fill()
    label = Label(scr, Rect(32, 0, 30, 1), 2)
    label.text = "Hello, World!"
    label = Label(scr, Rect(32, 1, 30, 2), 1)
    label.text = "How are you today?"
    label.text = "Extra large text that overflow from its boundaries"
    scr.refresh()
    scr.getkey()


if __name__ == "__main__":
    main()

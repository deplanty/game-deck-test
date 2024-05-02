import curses

from src.tui import Widget


class Tui(Widget):
    def __init__(self):
        super().__init__(None)
        self.scr = curses.initscr()
        self.children = list()
        Widget.main = self

    # Methods

    def update(self):
        for child in self.children:
            child._update()
        self.scr.refresh()

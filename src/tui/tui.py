import curses

from src.tui import Widget


class Tui(Widget):
    def __init__(self):
        super().__init__(None)
        self.scr = curses.initscr()
        curses.noecho()
        self.scr.clear()

        self.children = list()
        self.focus_widget = None

        Widget.main = self

    # Methods

    def update(self):
        for child in self.children:
            child._update()

        if self.focus_widget:
            result = self.focus_widget.focus()
            if result == "tab":
                self.focus_widget = self.focus_widget.focus_next

        self.scr.refresh()

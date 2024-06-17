import curses

from src.tui import Widget
from src.tui.style import Color, Style


class Tui(Widget):
    def __init__(self):
        # Init curses
        self.scr = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        curses.noecho()

        # Init this class as a Widget
        super().__init__(None)

        # Keyboard
        # FIXME: keypad(True) allows to detect keystrokes of the arrows.
        #        but it conflicts with other printable characters (same chr).
        #        Find something to manage this.
        self.scr.keypad(True)
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
                while True:
                    widget = self.focus_widget.focus_next
                    self.focus_widget = widget
                    if widget is None:
                        break
                    elif widget.visible:
                        break
            elif result == "tab_back":
                focused_widgets = self._get_list_widget_focus()
                index = focused_widgets.index(self.focus_widget)
                while True:
                    widget = focused_widgets[index -1]
                    if widget and widget.visible:
                        self.focus_widget = focused_widgets[index - 1]
                        break
                    else:
                        index -= 1

        self.scr.refresh()

    def _get_list_widget_focus(self):
        if self.focus_widget:
            cycle = list()
            current = self.focus_widget
            while current:
                cycle.append(current)
                current = current.focus_next
                if current in cycle:
                    current = None

            return cycle

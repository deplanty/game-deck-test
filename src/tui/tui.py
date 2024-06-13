import curses

from src.tui import Widget
from src.tui.style import Color, Style


class Tui(Widget):
    def __init__(self):
        super().__init__(None)
        self.scr = curses.initscr()
        # Colors
        curses.start_color()
        curses.use_default_colors()
        self._init_colors()
        # Keyboard
        curses.noecho()
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
                self.focus_widget = self.focus_widget.focus_next
            elif result == "tab_back":
                focused_widgets = self._get_list_widget_focus()
                index = focused_widgets.index(self.focus_widget)
                self.focus_widget = focused_widgets[index - 1]

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

    def _init_colors(self):
        """Initialize a small bunch of color_pairs.

        The colors and pairs and everything should be stored in a file.
        """

        curses.init_pair(Style.TEXT_PRIMARY, 33, -1)
        curses.init_pair(Style.TEXT_SECONDARY, 141, -1)
        curses.init_pair(Style.TEXT_SUCCESS, 34, -1)
        curses.init_pair(Style.TEXT_DANGER, 196, -1)
        curses.init_pair(Style.TEXT_WARNING, 214, -1)
        curses.init_pair(Style.TEXT_INFO, 37, -1)
        curses.init_pair(Style.TEXT_LIGHT, 252, -1)
        curses.init_pair(Style.TEXT_DARK, 234, -1)
        curses.init_pair(Style.TEXT_WHITE, 255, -1)

        curses.init_pair(Style.BG_PRIMARY, -1, 27)
        curses.init_pair(Style.BG_SECONDARY, -1, 5)
        curses.init_pair(Style.BG_SUCCESS, -1, 28)
        curses.init_pair(Style.BG_DANGER, -1, 160)
        curses.init_pair(Style.BG_WARNING, Color.BLACK, 214)
        curses.init_pair(Style.BG_INFO, -1, 30)
        curses.init_pair(Style.BG_LIGHT, Color.BLACK, 252)
        curses.init_pair(Style.BG_DARK, -1, 234)
        curses.init_pair(Style.BG_WHITE, -1, 255)

        curses.init_pair(Style.MUTE, 238, -1)

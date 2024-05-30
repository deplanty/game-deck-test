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
        """Initialize a small bunch of color_pairs."""

        curses.init_pair(Style.TEXT_PRIMARY, Color.PRIMARY, -1)
        curses.init_pair(Style.TEXT_SECONDARY, Color.SECONDARY, -1)
        curses.init_pair(Style.TEXT_SUCCESS, Color.SUCCESS, -1)
        curses.init_pair(Style.TEXT_DANGER, Color.DANGER, -1)
        curses.init_pair(Style.TEXT_WARNING, Color.WARNING, -1)
        curses.init_pair(Style.TEXT_INFO, Color.INFO, -1)
        curses.init_pair(Style.TEXT_MUTED, 238, -1)

        curses.init_pair(Style.BG_PRIMARY, Color.WHITE, Color.PRIMARY)
        curses.init_pair(Style.BG_SECONDARY, Color.WHITE, Color.SECONDARY)
        curses.init_pair(Style.BG_SUCCESS, Color.WHITE, Color.SUCCESS)
        curses.init_pair(Style.BG_DANGER, Color.WHITE, Color.DANGER)
        curses.init_pair(Style.BG_WARNING, Color.BLACK, Color.WARNING)
        curses.init_pair(Style.BG_INFO, Color.BLACK, Color.INFO)

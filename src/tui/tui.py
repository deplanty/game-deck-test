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
        # Clear the window. It's better to use scr.erase() rather than scr.clear() according to
        # this question: https://stackoverflow.com/questions/9653688/how-to-refresh-curses-window-correctly
        self.scr.erase()

        for child in self.children:
            child._update()

        if self.focus_widget:
            result = self.focus_widget._focus_run()

            if result == "tab":
                self.focus_widget = self._get_next_focus_widget()
            elif result == "tab_back":
                self.focus_widget = self._get_prev_focus_widget()

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

    def _get_next_focus_widget(self) -> Widget:
        current = self.focus_widget
        while True:
            current = current.focus_next
            if current is None:
                break
            elif current.visible:
                break
        return current
        

    def _get_prev_focus_widget(self) -> Widget:
        focused_widgets = self._get_list_widget_focus()

        index = focused_widgets.index(self.focus_widget)
        while True:
            widget = focused_widgets[index -1]
            if widget and widget.visible:
                return focused_widgets[index - 1]
            else:
                index -= 1
        

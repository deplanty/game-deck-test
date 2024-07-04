import curses

from src.tui import Signal, Widget, Label
from src.tui.style import Style
from src.tui.keys import Keys


class Button(Label):
    """
    A simple widget that can be focused and pressed.

    Signals:
        pressed: when the button is pressed.
    """

    def __init__(self, parent:Widget, text:str="", style_normal=Style.BG_LIGHT, style_hover=Style.BG_PRIMARY):
        super().__init__(parent, text, style=style_normal)
        self.style_normal = style_normal
        self.style_hover = style_hover

        self.pressed = Signal()

    def _on_focus(self):
        curses.cbreak()
        cursor_previous = curses.curs_set(0) # 0=invisible
        self.style = self.style_hover

        state = ""
        while state == "":
            self.update()
            key = self.getch()
            if key == Keys.RETURN:
                state = "ok"
                self.pressed.emit()
            elif key == Keys.TABLUATION:
                state = "tab"
            elif key == Keys.TABLUATION_BACK:
                state = "tab_back"

        curses.nocbreak()
        curses.curs_set(cursor_previous)
        self.style = self.style_normal

        return state

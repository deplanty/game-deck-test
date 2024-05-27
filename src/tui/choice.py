import curses

from src import tui


class Choice(tui.Widget):
    def __init__(self, parent:tui.Widget):
        super().__init__(parent)

        self.choices = list()
        self.ui_elements = list()
        self._current = 0

    @property
    def height_calc(self) -> int:
        return len(self.choices)

    @property
    def current(self) -> int:
        return self._current

    @current.setter
    def current(self, value) -> int:
        if value >= 0 and value < len(self.choices):
            self._current = value

    @property
    def choice(self) -> str:
        return self.choices[self.current]

    # Events

    def _on_focus(self) -> str:
        """
        This function is triggered when a widget gets the focus.

        Returns:
            str: The choice made.
        """

        curses.cbreak()
        while True:
            key = self.main.scr.getch()
            if key == curses.KEY_UP:
                print("UP")
                self.current -= 1
            elif key == curses.KEY_DOWN:
                print("DOWN")
                self.current += 1
            elif key == 10:
                print("RETURN")
                result = "ok"
                break
            elif key == 8:
                print("BACKSPACE")
            self.update()
        curses.nocbreak()

        return result

    # Methods Required

    def update(self):
        for i, label in enumerate(self.ui_elements):
            if self.current == i:
                label.text = "*" + self.choices[i]
            else:
                label.text = self.choices[i]
            label.update()

    # Methods

    def add_element(self, text:str):
        """Add an element that can bee chosen."""

        self.choices.append(text)
        label = tui.Label(self, text)
        label.pack()
        self.ui_elements.append(label)
        

    def add_elements(self, *texts):
        """Add several elements."""

        for text in texts:
            self.add_element(text)
        

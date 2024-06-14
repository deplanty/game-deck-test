from src import tui
from src.tui.style import Style

import curses


class SceneMainMenuUi(tui.Tui):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene

        self.frame_title = tui.LabelFrame(self)
        self.frame_title.pack()
        self.label_title = tui.Label(self.frame_title, text="GAME DECK TEST", align="center")
        self.label_title.style = Style.TEXT_WHITE.bold()
        self.label_title.pack()
        self.label_subtitle = tui.Label(self.frame_title, text="Main Menu", align="center")
        self.label_subtitle.pack()
        

        tui.Frame(self).pack()

        self.choice_menu = tui.Choice(self)
        self.choice_menu.pack()

    def update(self):
        for i, option in enumerate(self.scene.menu_options):
            self.choice_menu.add_label(option)

        super().update()


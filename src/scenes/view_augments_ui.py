from src import tui
from src.tui.style import Style


class SceneViewAugmentsUi(tui.Tui):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene

        self.frame_title = tui.LabelFrame(self)
        self.frame_title.pack()
        self.label_title = tui.Label(self.frame_title, text="GAME DECK TEST", align="center")
        self.label_title.pack()

        tui.Frame(self).pack()

        self.frame_augments = tui.Frame(self)
        self.frame_augments.pack(fill=True)
        self.choice_menu = tui.Choice(self.frame_augments)
        self.choice_menu.grid(0, 0)
        self.label_augment = tui.Label(self.frame_augments)
        self.label_augment.grid(0, 1)

    def update(self):
        self.choice_menu.reset_choices()
        for item in self.scene.menu_options:
            self.choice_menu.add_label(item)
        self.frame_augments.fill()

        super().update()

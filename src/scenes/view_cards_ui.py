from src import tui
from src.tui.style import Style


class SceneViewCardsUi(tui.Tui):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene

        self.frame_title = tui.LabelFrame(self)
        self.frame_title.pack()
        self.label_title = tui.Label(self.frame_title, text="GAME DECK TEST", align="center")
        self.label_title.pack()

        tui.Frame(self).pack()

        self.frame_cards = tui.Frame(self)
        self.frame_cards.pack(fill=True)
        self.choice_menu = tui.Choice(self.frame_cards)
        self.choice_menu.grid(0, 0)
        self.label_card = tui.Label(self.frame_cards)
        self.label_card.grid(0, 1)

    def update(self):
        self.choice_menu.reset_choices()
        for item in self.scene.menu_options:
            self.choice_menu.add_label(item)
        self.frame_cards.fill()

        super().update()

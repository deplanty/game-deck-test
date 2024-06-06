from src import tui


class SceneSelectHeroUi(tui.Tui):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene

        self.frame_title = tui.Frame(self, border=True)
        self.frame_title.pack()
        self.label_title = tui.Label(self.frame_title, text="GAME DECK TEST", align="center")
        self.label_title.pack()

        self.label_info = tui.Label(self, "Select your hero for this journey:")
        self.label_info.pack()

        self.choice_heroes = tui.Choice(self)
        self.choice_heroes.pack()

        tui.Frame(self).pack()

        self.label_hero_description = tui.Label(self, prefix="Selected hero:\n")
        self.label_hero_description.pack()

    def update(self):
        for i, hero in enumerate(self.scene.heroes):
            self.choice_heroes.add_label(str(hero))
        self.choice_heroes.add_label("Quit")

        super().update()

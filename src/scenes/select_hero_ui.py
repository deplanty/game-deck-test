from src import tui


class SceneSelectHeroUi(tui.Tui):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene

        self.label_title = tui.Label(self, "Select your hero for this journey:")
        self.label_title.pack()

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

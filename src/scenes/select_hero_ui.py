from src import tui
from src.tui.style import Style


class SceneSelectHeroUi(tui.Tui):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene

        self.frame_title = tui.LabelFrame(self)
        self.frame_title.pack()
        self.label_title = tui.Label(self.frame_title, text="GAME DECK TEST", align="center")
        self.label_title.pack()

        tui.Frame(self).pack()

        frame = tui.Frame(self)
        frame.pack(fill=True)

        frame_select = tui.Frame(frame)
        frame_select.grid(0, 0)

        self.label_info = tui.Label(frame_select, "Select your hero for this journey:")
        self.label_info.pack()

        self.choice_heroes = tui.Choice(frame_select)
        self.choice_heroes.pack()

        frame_description = tui.Frame(frame)
        frame_description.grid(0, 1)

        self.label_hero_description = tui.Label(frame_description, prefix="Selected hero:\n")
        self.label_hero_description.pack()
        self.label_cards_list = tui.Label(frame_description, prefix="Cards in deck:\n")
        self.label_cards_list.pack(fill=True)

        self.choice_heroes.focus_next = self.choice_heroes

    def update(self):
        self.choice_heroes.reset_choices()
        for i, hero in enumerate(self.scene.heroes):
            self.choice_heroes.add_label(str(hero))
        self.choice_heroes.add_label("Back", style=Style.TEXT_WARNING)

        super().update()

from src import tui
from src.tui.style import Style


class SceneSelectEncounterUi(tui.Tui):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene

        self.frame_title = tui.LabelFrame(self)
        self.frame_title.pack()
        self.label_title = tui.Label(self.frame_title, text="GAME DECK TEST", align="center")
        self.label_title.pack()

        self.label_info = tui.Label(self, "List of encounters:")
        self.label_info.pack()

        self.choice_encounter = tui.Choice(self)
        self.choice_encounter.pack()

    def update(self):
        for i, encounter in enumerate(self.scene.encounters):
            self.choice_encounter.add_label(str(encounter))
        self.choice_encounter.add_label("Back", style=Style.TEXT_WARNING)
        
        super().update()

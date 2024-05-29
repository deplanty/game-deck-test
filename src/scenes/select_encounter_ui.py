from src import tui


class SceneSelectEncounterUi(tui.Tui):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene

        self.label = tui.Label(self, "List of encounters:")
        self.label.pack()

        self.choice_encounter = tui.Choice(self)
        self.choice_encounter.pack()

    def update(self):
        for i, encounter in enumerate(self.scene.encounters):
            self.choice_encounter.add_label(str(encounter))
        self.choice_encounter.add_label("Quit")
        
        super().update()

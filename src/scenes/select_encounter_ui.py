from src import tui


class SceneSelectEncounterUi(tui.Tui):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene

        self.label_encounter = tui.Label(self)
        self.label_encounter.grid(0)

        self.entry = tui.Entry(self, "Select encounter")
        self.entry.grid(1, rowspan=4)

        self.entry.focus_set()

    def update(self):
        encounters = ["List of encounters:"]
        for i, encounter in enumerate(self.scene.encounters):
            encounters.append(f"   {i}. {encounter}.")
        encounters.append("   'quit' to stop.")
        self.label_encounter.text = "\n".join(encounters)
        
        super().update()

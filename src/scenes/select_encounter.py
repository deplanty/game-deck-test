import src.singleton as sgt
from src.scenes import Scene, SceneCombat

from .select_encounter_ui import SceneSelectEncounterUi


class SceneSelectEncounter(Scene):
    def __init__(self):
        super().__init__()

        self.encounters = sgt.all_encounters

        self.ui = SceneSelectEncounterUi(self)
        
    def run(self):
        """Run this scene loop."""

        answer = ""
        scene = None
        while answer != "quit":
            self.ui.update()
            answer = self.ask_input()
            if isinstance(answer, int):
                selected = self.encounters[answer]
                scene = SceneCombat(selected.name)
                answer = "quit"
        return scene

    def ask_input(self) -> int|str:
        action = self.ui.entry.text
        if action.isnumeric():
            return int(action)
        else:
            return action

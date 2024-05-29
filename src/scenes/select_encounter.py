import src.singleton as sgt
from src.scenes import Scene, SceneCombat

from .select_encounter_ui import SceneSelectEncounterUi


class SceneSelectEncounter(Scene):
    def __init__(self):
        super().__init__()

        self.encounters = sgt.all_encounters

        self.ui = SceneSelectEncounterUi(self)
        self.ui.choice_encounter.selected.connect(self._on_choice_encouter_selected)
        
    def run(self):
        """Run this scene loop.
        
        The loop is carried by the choice selector.
        When the choice is made, the loop ends and the scene switch to the selected encounter.
        """

        self.ui.choice_encounter.focus_set()
        self.ui.update()

        return self.scene

    # Events

    def _on_choice_encouter_selected(self):
        if self.ui.choice_encounter.choice == "Quit":
            self.scene = None
        else:
            index = self.ui.choice_encounter.current
            selected = self.encounters[index]
            self.scene = SceneCombat(selected.name)

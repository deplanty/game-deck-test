import src.singleton as sgt
from src import scenes

from .select_encounter_ui import SceneSelectEncounterUi


class SceneSelectEncounter(scenes.Scene):
    def __init__(self):
        super().__init__()

        self.encounters = list()
        for iid in sgt.path_step_current.encounters:
            self.encounters.append(sgt.encounter_from_id(iid))

        self.ui = SceneSelectEncounterUi(self)
        self.ui.choice_encounter.selected.connect(self._on_choice_encouter_selected)
        
    def run(self):
        """Run this scene loop.
        
        The loop is carried by the choice selector.
        When the choice is made, the loop ends and the scene switch to the selected encounter.
        """

        self.ui.choice_encounter.focus_set()

        self.scene_next = None
        while self.scene_next is None:
            self.ui.update()

        return self.scene_next

    # Events

    def _on_choice_encouter_selected(self):
        if self.ui.choice_encounter.choice == "Back":
            self.scene_next = scenes.SceneSelectHero()
        else:
            index = self.ui.choice_encounter.current
            selected = self.encounters[index]
            self.scene_next = scenes.SceneCombat(selected.iid)

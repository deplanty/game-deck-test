import src.singleton as sgt
from src import scenes

from .select_encounter_ui import SceneSelectEncounterUi


class SceneSelectEncounter(scenes.Scene):
    def __init__(self):
        super().__init__()

        self.encounters = sgt.path_step_current.get_encounters()

        self.ui = SceneSelectEncounterUi(self)
        self.ui.choice_encounter.selected.connect(self._on_choice_encouter_selected)
        self.ui.button_back.pressed.connect(self._on_button_back_pressed)

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
        index = self.ui.choice_encounter.current
        selected = self.encounters[index]
        sgt.path_step_current.select_encounter(selected)
        self.scene_next = scenes.SceneCombat()

    def _on_button_back_pressed(self):
        self.scene_next = scenes.SceneSelectHero()

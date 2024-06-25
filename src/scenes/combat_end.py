import src.singleton as sgt
from src import scenes
from src.tui.style import Style

from .combat_end_ui import SceneCombatEndUi


class SceneCombatEnd(scenes.Scene):
    def __init__(self, result:str):
        super().__init__()

        self.result = result

        self.ui = SceneCombatEndUi(self)

    def run(self):
        if self.result == "victory":
            self.ui.label_result.style = Style.TEXT_SUCCESS
            self.ui.label_result.text = sgt.text_victory
        elif self.result == "defeat":
            self.ui.label_result.style = Style.TEXT_WARNING
            self.ui.label_result.text = sgt.text_defeat
        self.ui.choice_options.add_label("Upgrade a card")
        self.ui.choice_options.add_label("Add a new card")
        self.ui.choice_options.add_label("Continue")
        self.ui.choice_options.add_label("Main menu")
        self.ui.choice_options.add_label("Quit")

        scene = None
        while scene is None:
            self.ui.choice_options.focus_set()
            self.ui.update()

            if self.ui.choice_options.choice == "Main menu":
                scene = scenes.SceneMainMenu()
            elif self.ui.choice_options.choice == "Quit":
                scene = False
            elif self.ui.choice_options.choice == "Continue":
                scene = scenes.SceneSelectEncounter()
            elif self.ui.choice_options.choice == "Upgrade a card":
                ...
            elif self.ui.choice_options.choice == "Add a nex card":
                ...

        return scene

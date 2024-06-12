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
            self.ui.label_result.set_style(Style.TEXT_SUCCESS)
            self.ui.label_result.text = sgt.text_victory
        elif self.result == "defeat":
            self.ui.label_result.set_style(Style.TEXT_WARNING)
            self.ui.label_result.text = sgt.text_defeat
        self.ui.choice_options.add_label("Main menu")
        self.ui.choice_options.add_label("Quit")

        loop = True
        while loop:
            self.ui.choice_options.focus_set()
            self.ui.update()

            if self.ui.choice_options.choice == "Main menu":
                scene = scenes.SceneMainMenu()
                loop = False
            elif self.ui.choice_options.choice == "Quit":
                scene = None
                loop = False

        return scene

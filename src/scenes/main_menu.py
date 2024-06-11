import src.singleton as sgt
from src.scenes import Scene, SceneSelectHero

from .main_menu_ui import SceneMainMenuUi


class SceneMainMenu(Scene):
    def __init__(self):
        super().__init__()

        self.menu_options = ["Play", "Settings", "Quit"]
        self.ui = SceneMainMenuUi(self)
        self.ui.choice_menu.selected.connect(self._on_choice_menu_selected)

    def run(self):
        self.ui.choice_menu.focus_set()
        self.ui.update()
        
        return self.scene

    # Events

    def _on_choice_menu_selected(self):
        item = self.ui.choice_menu.choice
        if item == "Play":
            self.scene = SceneSelectHero()
        elif item == "Quit":
            self.scene = None
        else:
            self.scene = None

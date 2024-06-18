import src.singleton as sgt
from src.scenes import Scene, SceneSelectHero, SceneViewCards

from .main_menu_ui import SceneMainMenuUi


class SceneMainMenu(Scene):
    def __init__(self):
        super().__init__()

        self.menu_options = ["Play", "Show all cards", "Settings", "Quit"]
        self.ui = SceneMainMenuUi(self)
        self.ui.choice_menu.selected.connect(self._on_choice_menu_selected)

    def run(self):
        self.ui.choice_menu.focus_set()

        self.scene_next = None
        while self.scene_next is None:
            self.ui.update()
        
        return self.scene_next

    # Events

    def _on_choice_menu_selected(self):
        item = self.ui.choice_menu.choice
        if item == "Play":
            self.scene_next = SceneSelectHero()
        elif item == "Show all cards":
            self.scene_next = SceneViewCards()
        elif item == "Quit":
            self.scene_next = False
        else:
            self.scene_next = False

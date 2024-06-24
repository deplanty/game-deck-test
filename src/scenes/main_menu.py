import src.singleton as sgt
from src import scenes

from .main_menu_ui import SceneMainMenuUi


class SceneMainMenu(scenes.Scene):
    def __init__(self):
        super().__init__()

        self.menu_options = ["Play", "Show all cards", "Show all augments", "Settings", "Quit"]
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
            self.scene_next = scenes.SceneSelectHero()
        elif item == "Show all cards":
            self.scene_next = scenes.SceneViewCards()
        elif item == "Show all augments":
            self.scene_next = scenes.SceneViewAugments()
        elif item == "Quit":
            self.scene_next = False
        else:
            self.scene_next = False

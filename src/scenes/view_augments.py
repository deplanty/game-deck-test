import src.singleton as sgt
from src import scenes

from .view_augments_ui import SceneViewAugmentsUi


class SceneViewAugments(scenes.Scene):
    def __init__(self):
        super().__init__()

        self.list_augments = list(sgt.all_augments.values())
        self.menu_options = list()

        self.ui = SceneViewAugmentsUi(self)
        self.ui.choice_menu.hovered.connect(self._on_choice_menu_hovered)

    def run(self):
        loop = True
        while loop:
            self.menu_options.clear()
            for augment in self.list_augments:
                self.menu_options.append(augment.name)

            self.menu_options.append("Return to main menu")

            # Wait for user input and process them
            self.ui.choice_menu.focus_set()
            self.ui.update()

            item = self.ui.choice_menu.choice
            if item == "Return to main menu":
                scene = scenes.SceneMainMenu()
                loop = False
                
            
        return scene

    def _on_choice_menu_hovered(self):
        index = self.ui.choice_menu.current
        item = self.ui.choice_menu.choice_current
        if item == "Return to main menu":
            self.ui.label_augment.text = ""
        else:
            augment = self.list_augments[index]
            self.ui.label_augment.text = augment.info
        self.ui.label_augment.update()

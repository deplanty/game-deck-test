import src.singleton as sgt
from src.scenes import Scene, SceneSelectEncounter

from .select_hero_ui import SceneSelectHeroUi


class SceneSelectHero(Scene):
    def __init__(self):
        super().__init__()

        self.heroes = sgt.all_heroes
        self.ui = SceneSelectHeroUi(self)
        self.ui.choice_heroes.selected.connect(self._on_choice_hero_selected)
        self.ui.choice_heroes.hovered.connect(self._on_choice_hero_hovered)

    def run(self):
        self.ui.choice_heroes.focus_set()
        self.ui.update()
        
        return self.scene

    # Events

    def _on_choice_hero_hovered(self):
        index = self.ui.choice_heroes.current
        if index < len(self.heroes):
            hero = self.heroes[index]
            self.ui.label_hero_description.text = hero.info
        else:
            self.ui.label_hero_description.text = ""
        self.ui.label_hero_description.update()

    def _on_choice_hero_selected(self):
        if self.ui.choice_heroes.choice == "Quit":
            self.scene = None
        else:
            index = self.ui.choice_heroes.current
            sgt.player = self.heroes[index]
            self.scene = SceneSelectEncounter()

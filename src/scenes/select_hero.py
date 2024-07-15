import src.singleton as sgt
from src import scenes

from .select_hero_ui import SceneSelectHeroUi


class SceneSelectHero(scenes.Scene):
    def __init__(self):
        super().__init__()

        self.heroes = sgt.all_heroes
        self.ui = SceneSelectHeroUi(self)
        self.ui.choice_heroes.selected.connect(self._on_choice_hero_selected)
        self.ui.choice_heroes.hovered.connect(self._on_choice_hero_hovered)
        self.ui.button_back.pressed.connect(self._on_button_back_pressed)

    def run(self):
        self.ui.choice_heroes.focus_set()

        self.scene_next = None
        while self.scene_next is None:
            self.ui.update()
        
        return self.scene_next

    # Events

    def _on_choice_hero_hovered(self):
        index = self.ui.choice_heroes.current
        if index < len(self.heroes):
            hero = self.heroes[index]
            self.ui.label_hero_description.text = hero.info
            self.ui.label_cards_list.text = "\n".join([card.name for card in hero.deck.deck])
        else:
            self.ui.label_hero_description.text = ""
            self.ui.label_cards_list.text = ""
        self.ui.label_hero_description.update()
        self.ui.label_cards_list.update()

    def _on_choice_hero_selected(self):
        index = self.ui.choice_heroes.current
        sgt.player = self.heroes[index].copy()
        sgt.path_step_current = sgt.path_step_from_id(0)
        sgt.path_step_current.init()
        self.scene_next = scenes.SceneSelectEncounter()

    def _on_button_back_pressed(self):
        self.scene_next = scenes.SceneMainMenu()

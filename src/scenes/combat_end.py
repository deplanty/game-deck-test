import src.singleton as sgt
from src import scenes
from src.tui.style import Style

from .combat_end_ui import SceneCombatEndUi


class SceneCombatEnd(scenes.Scene):
    def __init__(self, result:str):
        super().__init__()

        self.result = result

        sgt.player.deck.reform()
        self.cards_upgrade = sgt.player.deck.deck
        # Select from 3 random cards
        self.cards_add = sgt.get_random_cards(3)

        self.ui = SceneCombatEndUi(self)
        self.ui.choice_options.selected.connect(self._on_choice_options_selected)
        self.ui.popup_upgrade.selected.connect(self._on_popup_upgrade_selected)
        self.ui.popup_add.selected.connect(self._on_popup_add_selected)

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

        self.scene = None
        self.ui.choice_options.focus_set()
        while self.scene is None:
            self.ui.update()

        return self.scene

    def _on_choice_options_selected(self):
        if self.ui.choice_options.choice == "Main menu":
            self.scene = scenes.SceneMainMenu()
        elif self.ui.choice_options.choice == "Quit":
            self.scene = False
        elif self.ui.choice_options.choice == "Continue":
            self.scene = scenes.SceneSelectEncounter()
        elif self.ui.choice_options.choice == "Upgrade a card":
            self.ui.popup_upgrade.show()
            self.ui.popup_upgrade.focus_set()
        elif self.ui.choice_options.choice == "Add a new card":
            self.ui.popup_add.show()
            self.ui.popup_add.focus_set()

    def _on_popup_upgrade_selected(self):
        card = self.ui.popup_upgrade.card
        card.upgrade() 
        self.scene = scenes.SceneSelectEncounter()

    def _on_popup_add_selected(self):
        card = self.ui.popup_add.card
        sgt.player.add_card_from_id(card.iid)
        self.scene = scenes.SceneSelectEncounter()

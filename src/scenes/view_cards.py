import src.singleton as sgt
from src import scenes

from .view_cards_ui import SceneViewCardsUi


class SceneViewCards(scenes.Scene):
    def __init__(self):
        super().__init__()

        self.ui = SceneViewCardsUi(self)
        self.ui.choice_menu.hovered.connect(self._on_choice_menu_hovered)

        # Get the number of cards that can be shown at once
        self.show_n = self.ui.frame_cards.height - 4
        self.show_start = 0
        self.menu_options = list()
        

    def run(self):
        # Loop
        loop = True
        while loop:
            # Show as much cards as possible
            self.menu_options.clear()
            show = min(len(sgt.all_cards) - self.show_start, self.show_n)
            for i in range(self.show_start, self.show_start + show):
                card = sgt.all_cards[i + 1]
                self.menu_options.append(card.name_full)

            # Show the page previous option only if there are already sole cards shown
            if self.show_start > 0:
                self.menu_options.append("Previous")

            # Show the page next option only if there are some more cards
            if self.show_start + show < len(sgt.all_cards):
                self.menu_options.append("Next")
            self.menu_options.append("Return to main menu")

            # Wait for user input and process the input
            self.ui.choice_menu.focus_set()
            self.ui.update()

            item = self.ui.choice_menu.choice
            if item == "Previous":
                self.show_start -= self.show_n
            elif item == "Next":
                self.show_start += show
            elif item == "Return to main menu":
                scene = scenes.SceneMainMenu()
                loop = False

        return scene

    # Events

    def _on_choice_menu_hovered(self):
        index = self.ui.choice_menu.current
        item = self.ui.choice_menu.choice_current
        if item in ["Previous", "Next", "Return to main menu"]:
            self.ui.label_card.text = ""
        else:
            card = sgt.all_cards[self.show_start + index + 1]
            self.ui.label_card.text = card.info_full
        self.ui.label_card.update()

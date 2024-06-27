from src import tui
from src.widgets import SelectCard


class SceneCombatEndUi(tui.Tui):
    def __init__(self, scene):
        super().__init__()

        self.scene = scene

        self.frame_title = tui.LabelFrame(self)
        self.frame_title.pack()
        self.label_title = tui.Label(self.frame_title, text="GAME DECK TEST", align="center")
        self.label_title.pack()

        self.frame_main = tui.Frame(self)
        self.frame_main.pack()

        # Result frame
        self.label_result = tui.Label(self.frame_main, align="center")
        self.label_result.pack()

        self.choice_options = tui.Choice(self.frame_main)
        self.choice_options.pack()

        # Popup upgrade card
        self.popup_upgrade = SelectCard(self, "Upgrade a card", scene.cards_upgrade)
        self.popup_upgrade.place(x=0.5, y=0.5, width=0.6, height=0.8, anchor="center")
        self.popup_upgrade.hide()

        # Popup select card to add
        self.popup_add = SelectCard(self, "Select a cart to add", scene.cards_add)
        self.popup_add.place(x=0.5, y=0.5, width=0.6, height=0.8, anchor="center")
        self.popup_add.hide()

from src import tui


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
        self.popup_upgrade = tui.LabelFrame(self, text="Upgrade a card")
        self.popup_upgrade.place(x=0.5, y=0.5, width=0.6, height=0.8, anchor="center")
        self.popup_upgrade.hide()
        self.choice_upgrade = tui.Choice(self.popup_upgrade)
        self.choice_upgrade.pack(fill=True)

        # Initialize values
        for card in scene.cards_upgrade:
            self.choice_upgrade.add_label(str(card))

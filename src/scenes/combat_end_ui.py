from src import tui


class SceneCombatEndUi(tui.Tui):
    def __init__(self, scene):
        super().__init__()

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

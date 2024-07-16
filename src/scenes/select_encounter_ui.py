from src import tui
from src.tui.style import Style
from src.widgets import CardPlayer


class SceneSelectEncounterUi(tui.Tui):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene

        self.frame_title = tui.LabelFrame(self)
        self.frame_title.pack()
        self.label_title = tui.Label(self.frame_title, text="GAME DECK TEST", align="center")
        self.label_title.pack()

        tui.Frame(self).pack()

        self.button_back = tui.Button(self, text=" <-- Back ")
        self.button_back.pack()

        frame = tui.Frame(self)
        frame.pack()

        self.choice_encounter = tui.ChoiceWidget(frame, "List of encounters:", columns=3)
        self.choice_encounter.grid(0, 1, columnspan=8)
        tui.Frame(frame).grid(0, 9)


        self.choice_encounter.focus_next = self.button_back
        self.button_back.focus_next = self.choice_encounter

    def update(self):
        self.choice_encounter.reset()
        for i, encounter in enumerate(self.scene.encounters):
            self.choice_encounter.add_widget(CardPlayer, encounter)
        
        super().update()

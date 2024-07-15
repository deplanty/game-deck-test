from src import tui
from src.tui.style import Style
from src.objects import Player


class CardPlayerUi:
    def __init__(self, widget:tui.LabelFrame):
        self.widget = widget
        self.widget.style_border = Style.NORMAL
        self.label_name = tui.Label(widget, align="center")
        self.label_name.pack()
        tui.HLine(widget).pack()
        self.label_hp = tui.Label(widget, prefix="HP: ")
        self.label_hp.pack()
        self.label_energy = tui.Label(widget, prefix="Energy: ")
        self.label_energy.pack()
        self.label_augment = tui.Label(widget, prefix="Augments: \n")
        self.label_augment.pack()

    def update(self, player:Player):
        self.label_name.text = player.name
        self.label_hp.text = player.health
        self.label_energy.text = player.energy
        if len(player.augments) > 0:
            self.label_augment.text = "\n".join(f"  - {a.name}" for a in player.augments)
        else:
            self.label_augment.hide()


class CardPlayer(tui.LabelFrame):
    def __init__(self, parent:tui.Widget, player:Player):
        super().__init__(parent)

        self.ui = CardPlayerUi(self)
        self.ui.update(player)
        self.update()

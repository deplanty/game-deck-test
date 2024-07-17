from src import tui
from src.tui.style import Style
from src.objects import Card


class CardCardUi:
    def __init__(self, widget:tui.LabelFrame):
        self.widget = widget
        self.widget.style_border = Style.NORMAL
        self.label_name = tui.Label(widget, align="center")
        self.label_name.pack()
        tui.HLine(widget).pack()
        self.label_cost = tui.Label(widget, prefix="Cost: ")
        self.label_cost.pack()
        tui.Frame(widget).pack()
        self.label_desc = tui.Label(widget)
        self.label_desc.pack()

    def update(self, card:Card):
        self.label_name.text = card.name
        self.label_cost.text = card.cost
        self.label_desc.text = card.description


class CardCard(tui.LabelFrame):
    def __init__(self, parent:tui.Widget, card:Card):
        super().__init__(parent)

        self.ui = CardCardUi(self)
        self.ui.update(card)
        self.update()

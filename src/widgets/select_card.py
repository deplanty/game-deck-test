from src import tui


class SelectCardUi:
    def __init__(self, parent):
        self.parent = parent

        self.choice_card = tui.Choice(parent)
        self.choice_card.grid(0, 0)
        self.label_card = tui.Label(parent, prefix="Current card:\n")
        self.label_card.grid(0, 1)

        # Initialize the values
        for card in parent.cards:
            self.choice_card.add_label(str(card))


class SelectCard(tui.LabelFrame):
    selected:tui.Signal

    def __init__(self, parent, title:str, cards:list):
        super().__init__(parent, text=title)
        self.cards = cards

        self.selected = tui.Signal()
        self.ui = SelectCardUi(self)
        self.ui.choice_card.selected.connect(self._on_choice_card_selected)
        self.ui.choice_card.hovered.connect(self._on_choice_card_hovered)

    @property
    def card(self):
        return self.cards[self.ui.choice_card.current]

    def _on_focus(self):
        self.ui.choice_card.focus_set()

    def _on_choice_card_selected(self):
        self.selected.emit()

    def _on_choice_card_hovered(self):
        self.ui.label_card.text = self.card.info_full
        self.ui.label_card.update()

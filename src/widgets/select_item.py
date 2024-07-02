from src import tui


class SelectItemUi:
    def __init__(self, parent, prefix_label:str=""):
        self.parent = parent

        self.choice = tui.Choice(parent)
        self.choice.grid(0, 0)
        self.label = tui.Label(parent, prefix=prefix_label)
        self.label.grid(0, 1)

        # Initialize the values
        for item in parent.items:
            self.choice.add_label(str(item))


class SelectItem(tui.LabelFrame):
    selected:tui.Signal

    def __init__(self, parent, title:str, items:list):
        super().__init__(parent, text=title)
        self.items = items

        self.selected = tui.Signal()
        self.ui = SelectItemUi(self)
        self.ui.choice.selected.connect(self._on_choice_selected)
        self.ui.choice.hovered.connect(self._on_choice_hovered)

    @property
    def item(self):
        return self.items[self.ui.choice.current]

    def _on_focus(self):
        self.ui.choice.focus_set()

    def _on_choice_selected(self):
        self.selected.emit()

    def _on_choice_hovered(self):
        self.ui.label.text = self.item.info
        self.ui.label.update()

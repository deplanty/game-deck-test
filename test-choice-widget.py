from src import tui
from src.tui.style import Style


class Card(tui.LabelFrame):
    def __init__(self, parent:tui.Widget, value:str, color:str):
        super().__init__(parent)

        self.value = value
        self.color = color

        self.style_selected = Style.TEXT_PRIMARY
        self.style_idle = Style.MUTE

        self.label_value = tui.Label(self, text=self.value)
        self.label_value.pack()
        self.label_color = tui.Label(self, text=self.color)
        self.label_color.pack()

    def __str__(self):
        return f"{self.value}, {self.color}"


def _on_button_exit_pressed():
    global loop
    loop = False


root = tui.Tui()

button_exit = tui.Button(root, "Exit")
button_exit.pack()

choice_widget = tui.ChoiceWidget(root, "What will you do?", 4)
choice_widget.pack()
choice_widget.add_widget(Card, "As", "Heart")
choice_widget.add_widget(Card, "2", "Spade")
choice_widget.add_widget(Card, "3", "Heart")
choice_widget.add_widget(Card, "4", "Diamond")
choice_widget.add_widget(Card, "5", "Spade")
choice_widget.add_widget(Card, "6", "Spade")

button_exit.focus_set()
button_exit.focus_next = choice_widget
choice_widget.focus_next = button_exit

button_exit.pressed.connect(_on_button_exit_pressed)

loop = True
while loop:
    root.update()
    

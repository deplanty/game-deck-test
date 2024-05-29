import curses

from src import tui


def update_label():
    global choice_shape
    global choice_element
    global choice_trait
    global label

    label.text = f"Shape: {choice_shape.choice}\nElement: {choice_element.choice}\nTrait: {choice_trait.choice}"


root = tui.Tui()

frame_choices = tui.Frame(root)
frame_choices.pack()

choice_shape = tui.Choice(frame_choices)
choice_shape.add_labels("Triangle", "Square", "Pentagon", "Hexagon")
choice_shape.grid(0, 0)
choice_shape.focus_set()
choice_shape.selected.connect(update_label)

choice_element = tui.Choice(frame_choices)
choice_element.add_labels("Water", "Fire", "Earth", "Wind", "Ice")
choice_element.grid(0, 1)
choice_element.selected.connect(update_label)

choice_trait = tui.Choice(frame_choices)
choice_trait.add_labels("Soft", "Hard")
choice_trait.add_label("Lorem ipsum dolor sit amet." * 5)
choice_trait.grid(0, 2)
choice_trait.selected.connect(update_label)

tui.Frame(root).pack()

entry = tui.Entry(root)
entry.pack()

tui.Frame(root).pack()

label = tui.Label(root)
update_label()
label.pack()

choice_shape.focus_next = choice_element
choice_element.focus_next = choice_trait
choice_trait.focus_next = entry
entry.focus_next = choice_shape

while True:
    root.update()
    if entry.text == "exit":
        break   

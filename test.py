import curses

from src import tui


def on_choice_shape_selected():
    global label
    global choice_shape

    label.text += choice_shape.choice


root = tui.Tui()

frame_choices = tui.Frame(root)
frame_choices.pack()

choice_shape = tui.Choice(frame_choices)
choice_shape.add_labels("Triangle", "Square", "Pentagon", "Hexagon")
choice_shape.grid(0, 0)
choice_shape.focus_set()
choice_shape.selected.connect(on_choice_shape_selected)

choice_element = tui.Choice(frame_choices)
choice_element.add_labels("Water", "Fire", "Earth", "Wind", "Ice")
choice_element.grid(0, 1)

choice_trait = tui.Choice(frame_choices)
choice_trait.add_labels("Soft", "Hard")
choice_trait.add_label("Lorem ipsum dolor sit amet." * 5)
choice_trait.grid(0, 2)

tui.Frame(root).pack()

entry = tui.Entry(root)
entry.pack()

tui.Frame(root).pack()

label = tui.Label(root)
label.pack()

choice_shape.focus_next = choice_element
choice_element.focus_next = choice_trait
choice_trait.focus_next = entry
entry.focus_next = choice_shape

while True:
    root.update()
    if entry.text == "exit":
        break   

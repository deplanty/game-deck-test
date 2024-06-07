import curses

from src import tui


def update_label():
    global choice_shape
    global choice_element
    global choice_trait
    global label_shape
    global label_element
    global label_trait

    label_shape.text = choice_shape.choice
    label_element.text = choice_element.choice
    label_trait.text = choice_trait.choice


root = tui.Tui()

frame_title = tui.LabelFrame(root)
frame_title.pack()
label_title_left = tui.Label(frame_title, text="Title Left", align="left")
label_title_left.pack()
label_title = tui.Label(frame_title, text="Title", align="center")
label_title.pack()
label_title_right = tui.Label(frame_title, text="Title right", align="right")
label_title_right.pack()

frame_choices = tui.LabelFrame(root, text="Hello")
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
choice_trait.add_label("Lorem ipsum dolor sit amet." * 5)
choice_trait.add_labels("Soft", "Hard")
choice_trait.grid(0, 2)
choice_trait.selected.connect(update_label)

tui.Frame(root).pack()

entry = tui.Entry(root)
entry.pack()

tui.Frame(root).pack()

label_shape = tui.Label(root, prefix="Shape: ", suffix=".")
label_shape.pack()
label_element = tui.Label(root, prefix="Element: ", suffix="?")
label_element.pack()
label_trait = tui.Label(root, prefix="Trait: ", suffix="!")
label_trait.pack()

update_label()

choice_shape.focus_next = choice_element
choice_element.focus_next = choice_trait
choice_trait.focus_next = entry
entry.focus_next = choice_shape

while True:
    root.update()
    if entry.text == "exit":
        break   

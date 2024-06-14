import curses

from src import tui
from src.tui.style import Color, Style


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

Style.add("custom-text", fg=Color.WHITE, bg=Color.AZURE)
Style.add("custom-border", fg=Color.AZURE)

frame_title = tui.LabelFrame(root)
frame_title.pack()
label_title_left = tui.Label(frame_title, text="Title Left", align="left")
label_title_left.style.bold()
label_title_left.pack()
label_title_center = tui.Label(frame_title, text="Title Center", align="center")
label_title_center.style.bold()
label_title_center.pack()
label_title_right = tui.Label(frame_title, text="Title Right", align="right")
label_title_right.style.bold()
label_title_right.pack()

frame_style = tui.LabelFrame(root, text="Styles")
frame_style.pack()
tui.Label(frame_style, "Text primary", style=Style.TEXT_PRIMARY).grid(0, 0)
tui.Label(frame_style, "Text secondary", style=Style.TEXT_SECONDARY).grid(1, 0)
tui.Label(frame_style, "Text success", style=Style.TEXT_SUCCESS).grid(2, 0)
tui.Label(frame_style, "Text danger", style=Style.TEXT_DANGER).grid(3, 0)
tui.Label(frame_style, "Text warning", style=Style.TEXT_WARNING).grid(4, 0)
tui.Label(frame_style, "Text info", style=Style.TEXT_INFO).grid(5, 0)
tui.Label(frame_style, "Background primary", style=Style.BG_PRIMARY).grid(0, 1)
tui.Label(frame_style, "Background secondary", style=Style.BG_SECONDARY).grid(1, 1)
tui.Label(frame_style, "Background success", style=Style.BG_SUCCESS).grid(2, 1)
tui.Label(frame_style, "Background danger", style=Style.BG_DANGER).grid(3, 1)
tui.Label(frame_style, "Background warning", style=Style.BG_WARNING).grid(4, 1)
tui.Label(frame_style, "Background info", style=Style.BG_INFO).grid(5, 1)
tui.Label(frame_style, "Text light", style=Style.TEXT_LIGHT).grid(0, 2)
tui.Label(frame_style, "Text dark", style=Style.TEXT_DARK).grid(1, 2)
tui.Label(frame_style, "Text white", style=Style.TEXT_WHITE).grid(2, 2)
tui.Label(frame_style, "Background light", style=Style.BG_LIGHT).grid(3, 2)
tui.Label(frame_style, "Background dark", style=Style.BG_DARK).grid(4, 2)
tui.Label(frame_style, "Background white", style=Style.BG_WHITE).grid(5, 2)

frame_choices = tui.LabelFrame(root, text="Hello")
frame_choices.style_text = Style.get("custom-text")
frame_choices.style_border = Style.get("custom-border")
frame_choices.pack()

choice_shape = tui.Choice(frame_choices)
choice_shape.add_labels("Triangle", "Square", "Pentagon", "Hexagon")
choice_shape.grid(0, 0)
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

entry = tui.Entry(root, prefix="Input: ", placeholder="Enter text here")
entry.pack()

tui.Frame(root).pack()

label_shape = tui.Label(root, prefix="Shape: ", suffix=".")
label_shape.suffix_always = True
label_shape.pack()
label_element = tui.Label(root, prefix="Element: ", suffix="?")
label_element.pack()
label_trait = tui.Label(root, prefix="Trait: ", suffix="!")
label_trait.pack()

tui.Frame(root).pack()

label_big = tui.Label(root, align="center")
label_big.text = """\
 __      ___      _                   
 \ \    / (_)    | |                  
  \ \  / / _  ___| |_ ___  _ __ _   _ 
   \ \/ / | |/ __| __/ _ \| '__| | | |
    \  /  | | (__| || (_) | |  | |_| |
     \/   |_|\___|\__\___/|_|   \__, |
                                 __/ |
                                |___/ 
                                
"""
label_big.pack()

frame_fill = tui.Frame(root)
frame_fill.filler = "#"
frame_fill.pack(True)


update_label()

entry.focus_set()
choice_shape.focus_next = choice_element
choice_element.focus_next = choice_trait
choice_trait.focus_next = entry
entry.focus_next = choice_shape

while True:
    root.update()
    if entry.text == "exit":
        break   

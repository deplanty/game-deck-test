from src import tui

import curses
import textwrap


lorem = "Lorem ipsum dolor sit amet. " * 15

root = tui.Tui()

# Title
title = tui.Label(root, "Demo of the TUI widgets", align="center")
title.grid(0)

# Text on several columns
frame_text = tui.Frame(root)
frame_text.grid(1)
text = textwrap.wrap(lorem, len(lorem)//3)
for i, x in enumerate(text):
    tui.Label(frame_text, x).grid(0, i)

# Progress
progress = tui.Progressbar(root, maximum=200, align="center", display="value")
progress.grid(2)

# Frame
frame_1 = tui.Frame(root)
frame_1.grid(3)
# Fill frame
label = tui.Label(frame_1, "Row 0-1, Column 0")
label.grid(0, 0, rowspan=2)
label = tui.Label(frame_1, "Row 2, Column 0")
label.grid(2, 0)
label = tui.Label(frame_1, "Row 0, Column 1-2")
label.grid(0, 1, columnspan=2)
label = tui.Label(frame_1, "Row 1-2, Column 1")
label.grid(1, 1, rowspan=2)
label = tui.Label(frame_1, "Row 1-2, Column 2")
label.grid(1, 2, rowspan=2)

# Entry
entry = tui.Entry(root, "Placeholder")
entry.grid(4)
entry.focus_set()

entry_2 = tui.Entry(root, "")
entry_2.grid(5)


entry.focus_next = entry_2
entry_2.focus_next = entry
progress += 50

while True:
    root.update()
    if entry.text == "quit":
        break
    elif entry_2.text == "quit":
        break

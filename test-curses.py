from src import tui

import curses


lorem = "Lorem ipsum dolor sit amet. " * 15

root = tui.Tui()

# Title
title = tui.Label(root, lorem, align="center")
title.grid(0)

# First frame
frame_1 = tui.Frame(root)
frame_1.grid(1)
# Fill frame
for i in range(4):
    for j in range(2):
        label = tui.Label(frame_1, f"Cell({i}, {j})")
        label.grid(i, j)

# Second frame
frame_2 = tui.Frame(root)
frame_2.grid(2)
# Fill frame
for i in range(3):
    for j in range(5):
        label = tui.Label(frame_2, f"Cell({i}, {j})")
        label.grid(i, j)


root.update()
root.scr.getch()

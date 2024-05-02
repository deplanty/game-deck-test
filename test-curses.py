from src import tui

import curses


lorem = "Lorem ipsum dolor sit amet. " * 15

root = tui.Tui()

# Title
title = tui.Label(root, lorem, align="center")
title.grid(0)

# Progress
progress = tui.Progressbar(root, align="center", display="value")
progress.grid(1)

# Frame
frame_1 = tui.Frame(root)
frame_1.grid(2)
# Fill frame
for i in range(2):
    for j in range(2):
        label = tui.Label(frame_1, f"Cell({i}, {j})")
        label.grid(i, j)

# Entry
entry = tui.Entry(root)
entry.grid(3)
entry.focus_set()

for i in range(1):
    progress += 1
    root.update()
    # x = root.scr.getch()
    # print(x)
    # if x == 97:
    #     break

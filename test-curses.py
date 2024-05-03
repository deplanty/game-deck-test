from src import tui

import curses


lorem = "Lorem ipsum dolor sit amet. " * 15

root = tui.Tui()

# Title
title = tui.Label(root, lorem, align="center")
title.grid(0)

# Progress
progress = tui.Progressbar(root, maximum=200, align="center", display="value")
progress.grid(1)

# Frame
frame_1 = tui.Frame(root)
frame_1.grid(2)
# Fill frame
label = tui.Label(frame_1, "Row 0-1, Column 0")
label.filler = "."
label.grid(0, 0, rowspan=2)
label = tui.Label(frame_1, "Row 2, Column 0")
label.filler = "_"
label.grid(2, 0)
label = tui.Label(frame_1, "Row 0, Column 1-2")
label.filler = "_"
label.grid(0, 1, columnspan=2)
label = tui.Label(frame_1, "Row 1-2, Column 1")
label.filler = "-"
label.grid(1, 1, rowspan=2)
label = tui.Label(frame_1, "Row 1-2, Column 2")
label.grid(1, 2, rowspan=2)


# Entry
entry = tui.Entry(root)
entry.grid(3)
entry.focus_set()

for i in range(1):
    progress += 50
    root.update()
    # x = root.scr.getch()
    # print(x)
    # if x == 97:
    #     break

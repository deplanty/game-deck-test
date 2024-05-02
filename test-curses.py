from src import tui

import curses


lorem = "Lorem ipsum dolor sit amet. " * 15

root = tui.Tui()

frame_left = tui.Frame(root)
frame_left.grid(row=0, column=0)

label = tui.Label(frame_left, lorem)
label.grid(row=0, column=0)

frame_right = tui.Frame(root)
frame_right.grid(row=0, column=1)

label = tui.Label(frame_right, lorem)
label.grid(row=0, column=0)
label = tui.Label(frame_right, lorem)
label.grid(row=0, column=1)

# for j in range(20):
#     label = tui.Label(root, "123456789-123456789-123456789")
#     label.grid(row=0, column=j)



root.update()
root.scr.getch()

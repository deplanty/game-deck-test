from src import tui


root = tui.Tui()

title = tui.Label(root, "Title for the demo of the place layout", "center")
title.place(0, 0, 100, 1)

entry = tui.Entry(root, "Input")
entry.place(0, 1, 100, 1)
entry.focus_set()


while True:
    root.update()
    if entry.text == "quit":
        break

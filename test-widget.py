from src import tui


def update_label():
    global entry
    global label

    label.text = entry.text
    label.update()


root = tui.Tui()

entry = tui.Entry(root)
entry.pack()

tui.Frame(root).pack()

label = tui.Label(root, prefix="Entry value: ")
label.pack()

entry.focus_next = entry
entry.focus_set()
entry.changed.connect(update_label)

while True:
    root.update()

    if entry.text == "exit":
        break

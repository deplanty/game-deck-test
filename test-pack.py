from src import tui


lorem = "Lorem ipsum dolor sit amet."


root = tui.Tui()

label = tui.Label(root, "Demo for the pack layout", align="center")
label.pack()

tui.Frame(root).pack()

label = tui.Label(root, lorem * 15)
label.pack()

tui.Frame(root).pack()

progress = tui.Progressbar(root, 50, align="left", display="percent")
progress += 12
progress.pack()

tui.Frame(root).pack()

entry_1 = tui.Entry(root, "Input 1: ")
entry_1.pack()

entry_2 = tui.Entry(root, "Input 2: ")
entry_2.hide()
entry_2.pack()

entry_3 = tui.Entry(root, "Input 3: ")
entry_3.pack(fill=True)

tui.Label(root, "Last line").pack()

entry_1.focus_set()
entry_1.focus_next = entry_2
entry_2.focus_next = entry_3
entry_3.focus_next = entry_1

while True:
    root.update()
    if entry_1.text == "exit":
        break

    if entry_3.text == "hide":
        entry_2.hide()
    elif entry_3.text == "show":
        entry_2.show()

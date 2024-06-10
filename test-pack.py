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

entry = tui.Entry(root, "Input")
entry.pack(fill=True)

tui.Label(root, "Last line").pack()

entry.focus_set()
entry.focus_next = entry

while True:
    root.update()
    if entry.text == "exit":
        break

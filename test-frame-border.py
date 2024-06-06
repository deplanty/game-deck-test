from src import tui


root = tui.Tui()

entry = tui.Entry(root)
entry.pack()

frame = tui.Frame(root, border=True, border_title="Hey yo!")
frame.pack()
tui.Label(frame, text="Title").pack()
tui.Label(frame, text="Subtitle").pack()

frame_b = tui.Frame(root, border=True)
frame_b.pack()
tui.Label(frame_b, text="Title").pack()
tui.Label(frame_b, text="Subtitle").pack()

entry.focus_set()

while True:
    root.update()

    if entry.text == "exit":
        break

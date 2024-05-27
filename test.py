from src import tui


root = tui.Tui()

choice = tui.Choice(root)
choice.add_elements("Salut", "Plop", "Choix 3", "Choix 4")
choice.pack()
choice.focus_set()

while True:
    root.update()
    if choice.choice == "Plop":
        break

import curses

from src import tui


root = tui.Tui()
label = tui.Label(root)
label.text = "Select 'Plop' or write 'exit' in the entry.\n"
label.text += "Use TAB to navigate through the widgets."
label.pack()

tui.Frame(root).pack()

choice = tui.Choice(root)
choice.add_elements("Choix 1", "Choix 2", "Choix 3", "Choix 4", "Quit")
choice.pack()
choice.focus_set()

entry = tui.Entry(root)
entry.pack()

choice.focus_next = entry
entry.focus_next = choice

while True:
    root.update()
    if choice.choice == "Quit" or entry.text == "exit":
        break   

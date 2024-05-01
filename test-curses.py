from src import tui

import curses


root = tui.Tui()

label_long = tui.Label(root)
label_long.text = "Hello, World! I am a very long text that overflows from its boundaries."
label_long.grid(row=0, height=2)

label_short = tui.Label(root)
label_short.text = "Hello, World!"
label_short.grid(row=1, height=1)

label = tui.Label(root)
label.text = "Plop hehe"
label.grid(row=2)

root.update()
root.scr.getch()

import curses

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    n_colors = min(curses.COLORS, curses.COLOR_PAIRS)
    for i in range(1, n_colors):
        curses.init_pair(i, -1, i)
    try:
        for i in range(256):
            stdscr.addstr(str(i), curses.color_pair(i))

        col = 0
        row = 7
        stdscr.move(row, 0)
        for i in range(15):
            col += 1
            stdscr.addstr("  ", curses.color_pair(col))
        for i in range(36):
            row += 1
            stdscr.move(row, 0)
            for j in range(6):
                col += 1
                stdscr.addstr("  ", curses.color_pair(col))
        row += 1
        stdscr.move(row, 0)
        for i in range(24):
            col += 1
            stdscr.addstr("  ", curses.color_pair(col))
    except curses.ERR:
        # End of screen reached
        pass
    stdscr.getch()

curses.wrapper(main)

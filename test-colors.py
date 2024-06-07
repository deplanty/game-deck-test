import curses

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    n_colors = min(curses.COLORS, curses.COLOR_PAIRS)
    for i in range(1, n_colors):
        curses.init_pair(i, -1, i)
    try:
        for i in range(16):
            stdscr.addstr(f"{i:^4}", curses.color_pair(i))
        stdscr.move(1, 0)
        for i in range(16, 16 + 6*6*6):
            stdscr.addstr(f"{i:^4}", curses.color_pair(i))
        stdscr.move(7, 0)
        for i in range(16 + 6*6*6, 16 + 6*6*6 + 24):
            stdscr.addstr(f"{i:^4}", curses.color_pair(i))

        col = 0
        row = 9
        stdscr.move(row, 0)
        stdscr.addstr(f"{col + 1:3d} ")
        for i in range(15):
            col += 1
            stdscr.addstr("  ", curses.color_pair(col))
        for i in range(6):
            row += 1
            stdscr.move(row, 0)
            stdscr.addstr(f"{col + 1:3d} ")
            for j in range(6):
                for k in range(6):
                    col += 1
                    stdscr.addstr("  ", curses.color_pair(col))
                stdscr.addstr(" ")
        row += 1
        stdscr.move(row, 0)
        stdscr.addstr(f"{col + 1:3d} ")
        for i in range(24):
            col += 1
            stdscr.addstr("  ", curses.color_pair(col))
    except curses.ERR:
        # End of screen reached
        pass
    stdscr.getch()

curses.wrapper(main)

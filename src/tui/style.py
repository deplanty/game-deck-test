import curses

class Color:
    PRIMARY = 27
    SECONDARY = 239
    SUCCESS = 28
    DANGER = 124
    WARNING = 214
    INFO = 75

    WHITE = curses.COLOR_WHITE
    BLACK = curses.COLOR_BLACK


class Style:
    NORMAL = 0
    
    TEXT_PRIMARY = 1
    TEXT_SECONDARY = 2
    TEXT_SUCCESS = 3
    TEXT_DANGER = 4
    TEXT_WARNING = 5
    TEXT_INFO = 6
    TEXT_MUTED = 7

    BG_PRIMARY = 11
    BG_SECONDARY = 12
    BG_SUCCESS = 13
    BG_DANGER = 14
    BG_WARNING = 15
    BG_INFO = 16
    BG_LIGHT = 17
    BG_DARK = 18
    BG_WHITE = 19
    

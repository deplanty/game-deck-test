import curses

# TODO: Change how the styles are managed.
# TODO: Allow a simple way to add Bold, Italic, Underline, etc.

class Color:
    """Color number in the curses colormap."""

    WHITE = curses.COLOR_WHITE
    BLACK = curses.COLOR_BLACK


class Style:
    """Index for the `curses.init_pair`."""

    NORMAL = 0
    
    TEXT_PRIMARY = 1
    TEXT_SECONDARY = 2
    TEXT_SUCCESS = 3
    TEXT_DANGER = 4
    TEXT_WARNING = 5
    TEXT_INFO = 6
    TEXT_LIGHT = 7
    TEXT_DARK = 8
    TEXT_WHITE = 9

    BG_PRIMARY = 11
    BG_SECONDARY = 12
    BG_SUCCESS = 13
    BG_DANGER = 14
    BG_WARNING = 15
    BG_INFO = 16
    BG_LIGHT = 17
    BG_DARK = 18
    BG_WHITE = 19

    MUTE = 21
    

class BoxSimple:
    V = "|"
    H = "-"

    BORDER_H = H
    BORDER_V = V

    TL = "+"  # Top left
    TR = "+"  # Top right
    BL = "+"  # Bottom left
    BR = "+"  # Bottom right

    HB = "+"  # Horizontal bottom
    HT = "+"  # Horizontal top
    VL = "+"  # Vertical left
    VR = "+"  # Vertical right

    HV = "+"  # Horizontal vertical


class BoxClean:
    H = "─"
    V = "│"

    BORDER_H = H
    BORDER_V = V

    TL = "┌"  # Top left
    TR = "┐"  # Top right
    BL = "└"  # Bottom left
    BR = "┘"  # Bottom right

    HB = "┬"  # Horizontal bottom
    HT = "┴"  # Horizontal top
    VL = "┤"  # Vertical left
    VR = "├"  # Vertical right

    HV = "┼"  # Horizontal vertical


class BoxCleanBorder:
    H = "─"
    V = "│"

    BORDER_H = "═"
    BORDER_V = "║"

    TL = "╔"  # Top left
    TR = "╗"  # Top right
    BL = "╚"  # Bottom left
    BR = "╝"  # Bottom right

    HB = "╤"  # Horizontal bottom
    HT = "╧"  # Horizontal top
    VL = "╢"  # Vertical left
    VR = "╟"  # Vertical right

    HV = "┼"  # Horizontal vertical

import curses

# TODO: Change how the styles are managed.
# TODO: Allow a simple way to add Bold, Italic, Underline, etc.

class Color:
    """Color number in the curses colormap."""

    WHITE = curses.COLOR_WHITE
    BLACK = curses.COLOR_BLACK


class Pair:
    current_iid = 0

    def __init__(self, fg:int=-1, bg:int=-1, *modifiers):
        # The ID is an integer and is uniq
        self.iid = self.current_iid + 1
        self.increment_iid()

        self.fg = fg
        self.bg = bg
        self.modifiers = list(modifiers)

    @classmethod
    def increment_iid(cls):
        cls.current_iid += 1

    def apply(self) -> int:
        """Apply the style and return the corresponding curses identifier."""

        curses.init_pair(self.iid, self.fg, self.bg)
        style = curses.color_pair(self.iid)
        for modifier in self.modifiers:
            style |= modifier
        return style

    def bold(self):
        """Make the text bold."""

        self.modifiers.append(curses.A_BOLD)
        return self

    def italic(self):
        """Make the text italic."""

        self.modifiers.append(curses.A_ITALIC)
        return self

    def underline(self):
        """Underline the text."""
        
        self.modifiers.append(curses.A_UNDERLINE)
        return self

    def reverse(self):
        """Swap foreground and background colors."""

        self.modifiers.append(curses.A_REVERSE)
        return self


class Style:
    """Index for the `curses.init_pair`."""

    NORMAL = Pair()
    
    TEXT_PRIMARY = Pair(fg=33)
    TEXT_SECONDARY = Pair(fg=141)
    TEXT_SUCCESS = Pair(fg=34)
    TEXT_DANGER = Pair(fg=196)
    TEXT_WARNING = Pair(fg=214)
    TEXT_INFO = Pair(fg=37)
    TEXT_LIGHT = Pair(fg=252)
    TEXT_DARK = Pair(fg=234)
    TEXT_WHITE = Pair(fg=255)

    BG_PRIMARY = Pair(bg=27)
    BG_SECONDARY = Pair(bg=5)
    BG_SUCCESS = Pair(bg=28)
    BG_DANGER = Pair(bg=160)
    BG_WARNING = Pair(fg=Color.BLACK, bg=214)
    BG_INFO = Pair(bg=30)
    BG_LIGHT = Pair(fg=Color.BLACK, bg=252)
    BG_DARK = Pair(bg=234)
    BG_WHITE = Pair(fg=Color.BLACK, bg=255)

    MUTE = Pair(fg=238)

    _all_styles = {
        "normal": NORMAL,
        "text_primary": TEXT_PRIMARY,
        "bg_primary": BG_PRIMARY,
    }

    @classmethod
    def get(cls, key:str):
        return cls._all_styles.get(key, cls.NORMAL)


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

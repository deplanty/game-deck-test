class Grid:
    def __init__(self, row:int=0, column:int=0, rowspan:int=1, columnspan:int=1):
        self.set(row, column, rowspan, columnspan)

    def set(self, row:int=None, column:int=None, rowspan:int=None, columnspan:int=None):
        if row is not None: self.row = row
        if column is not None: self.column = column
        if rowspan is not None: self.rowspan = rowspan
        if columnspan is not None: self.columnspan = columnspan


class Pack:
    def __init__(self, fill:bool=False):
        self.set(fill)

    def set(self, fill:bool=None):
        if fill is not None: self.fill = fill


class Place:
    def __init__(self, x:int|float=None, y:int|float=None, width:int|float=1, height:int|float=1,
                 anchor:str="normal"):
        self.x :int= None
        self.y :int= None
        self.width :int= None
        self.height :int= None
        self.anchor :str= None

        self.set(x, y, width, height, anchor)

    def set(self, x:int|float=None, y:int|float=None, width:int|float=None, height:int|float=None,
            anchor:str=None):

        # Validate input parameters
        if isinstance(x, float) and (x < 0.0 or x > 1.0):
            raise ValueError("If x is relative: 0.0 <= x <= 1.0")
        if isinstance(y, float) and (y < 0.0 or y > 1.0):
            raise ValueError("If y is relative: 0.0 <= y <= 1.0")
        if isinstance(width, float) and (width < 0.0 or width > 1.0):
            raise ValueError("If width is relative: 0.0 <= width <= 1.0")
        if isinstance(height, float) and (height < 0.0 or height > 1.0):
            raise ValueError("If height is relative: 0.0 <= height <= 1.0")
        if anchor not in ["normal", "center"]:
            raise ValueError(f"anchor is {anchor} and should be one of [normal, center]")

        if x is not None: self.x = x
        if y is not None: self.y = y
        if width is not None: self.width = width
        if height is not None: self.height = height
        if anchor is not None: self.anchor = anchor

    def is_x_abs(self) -> bool:
        return isinstance(self.x, int)

    def is_y_abs(self) -> bool:
        return isinstance(self.y, int)

    def is_width_abs(self) -> bool:
        return isinstance(self.width, int)

    def is_height_abs(self) -> bool:
        return isinstance(self.height, int)

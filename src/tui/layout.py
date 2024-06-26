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
    def __init__(self, x:int=None, y:int=None, width:int=1, height:int=1,
                 relx:float=None, rely:float=None, anchor:str="normal"):
        self.x :int= None
        self.y :int= None
        self.width :int= None
        self.height :int= None
        self.relx :float= None
        self.rely :float= None
        self.anchor :str= None

        self.set(x, y, width, height, relx, rely, anchor)

    def set(self, x:int=None, y:int=None, width:int=None, height:int=None,
            relx:float=None, rely:float=None, anchor:str=None):

        if x is not None and relx is not None:
            raise ValueError("`x` and `relx` can't be used simultaneously.")
        if y is not None and rely is not None:
            raise ValueError("`y` and `rely` can't be used simultaneously.")

        if x is not None: self.x = x
        if y is not None: self.y = y
        if width is not None: self.width = width
        if height is not None: self.height = height
        if relx is not None: self.relx = relx
        if rely is not None: self.rely = rely
        if anchor is not None: self.anchor = anchor

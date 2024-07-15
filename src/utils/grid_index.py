class GridIndex:
    def __init__(self, index:int=0, columns:int=1, total:int=0):
        self.total = total
        self.index = index
        self.columns = columns

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, value:int):
        if value < 0:
            self._index = 0
        elif self.total == 0:
            self._index = 0
        elif value >= self.total:
            self._index = self.total - 1
        else:
            self._index = value

    @property
    def row(self) -> int:
        return self.index // self.columns

    @row.setter
    def row(self, row:int):
        col = self.column
        if 0 <= row:
            self.index = row * self.columns + self.column
        if self.column != col:
            self.column = col

    @property
    def column(self) -> int:
        return self.index % self.columns

    @column.setter
    def column(self, column:int):
        if 0 <= column < self.columns:
            self.index = self.row * self.columns + column

    @property
    def rowcol(self) -> tuple[int]:
        return self.row, self.column

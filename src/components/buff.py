class Buff:
    def __init__(self, name:str, value:int=0):
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"Buff({self.name})"

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, value:int):
        self.value += value
        return self

    def __radd__(self, value:int) -> int:
        return value + self.value

    def __sub__(self, value:int):
        self.value -= value
        if self.value < 0:
            self.value = 0
        return self

    def __rsub__(self, value:int) -> int:
        return value - self.value

    def __lt__(self, value:int) -> bool:
        return self.value < value

    def __le__(self, value:int) -> bool:
        return self.value <= value

    def __gt__(self, value:int) -> bool:
        return self.value > value

    def __ge__(self, value:int) -> bool:
        return self.value >= value
        
    # Properties

    @property
    def info(self) -> str:
        if self.value == 0:
            return None
        else:
            return f"{self.name} = {self.value}"

from src.utils import Signal


class Health:
    """
    The health of an entity.

    Args:
        maximum (int): Maximum health possible.

    Signals:
    """

    hurt:Signal
    heal:Signal
    dead:Signal

    
    def __init__(self, maximum:int):
        self.maximum = maximum
        self.current = self.maximum

        # Signals
        self.hurt = Signal()
        self.heal = Signal()
        self.dead = Signal()

    def __str__(self) -> str:
        return f"Health {self.current}/{self.maximum}"

    def __add__(self, value:int):
        self.current += value
        self.current = min(self.current, self.maximum)
        self.heal.emit()
        return self

    def __sub__(self, value:int):
        self.current -= value
        self.current = max(self.current, 0)
        self.hurt.emit()
        if self.current == 0:
            self.dead.emit()
        return self

    # Properties

    @property
    def percent(self) -> float:
        return self.current / self.maximum

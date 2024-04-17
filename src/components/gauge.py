from src.utils import Signal


class Gauge:

    filled:Signal  # When the gauge fills
    emptied:Signal  # When the gauge empties
    depleted:Signal  # When the gauge is empty
    
    def __init__(self, maximum:int):
        self._maximum = maximum
        self.current = maximum

        # Signals
        filled = Signal()
        emptied = Signal()
        depleted = Signal()

    def __str__(self) -> str:
        return f"{self.current}/{self.maximum}"

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, value:int):
        self.current += value
        self.filled.emit()
        return self

    def __sub__(self, value:int):
        self.current -= value
        if self.current <= 0:
            self.depleted.emit()
            self.current = 0
        return self
    
    # Properties

    @property
    def percent(self) -> float:
        return self.current / self.maximum

    @property
    def maximum(self) -> int:
        return self._maximum

    @maximum.setter
    def maximum(self, value:int):
        self._maximum = value

    # Methods

    def refill(self):
        """Set the current value to its maximum."""
        
        self.current = self.maximum
        self.fill.emit()

    def empty(self):
        """Set the current value to its minimum."""
        
        self.current = 0
        self.empty.emit()

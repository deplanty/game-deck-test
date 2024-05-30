from src.utils import Signal


class Gauge:
    """
    Represents a gauge that can be used for several objects: Health, Energy, ...

    Args:
        maximum (int): The maximum value of the gauge.

    Signals:
        changed: Emits when the current value is changed.
    """

    def __init__(self, maximum:int):
        self.current = maximum
        self.maximum = maximum
        self._allow_overflow = False

        # Signals
        self.changed = Signal()  # When the value changed
        
    def __str__(self) -> str:
        return f"{self.current}/{self.maximum}"

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, value:int):
        self.current += value
        if not self._allow_overflow and self.current > self.maximum:
            self.current = self.maximum
        self.changed.emit()
        return self

    def __sub__(self, value:int):
        self.current -= value
        if self.current <= 0:
            self.current = 0
        self.changed.emit()
        return self

    def __eq__(self, value:int) -> bool:
        return self.current == value

    def __lt__(self, value:int) -> bool:
        return self.current < value

    def __le__(self, value:int) -> bool:
        return self.current <= value

    def __gt__(self, value:int) -> bool:
        return self.current > value
    
    def __ge__(self, value:int) -> bool:
        return self.current >= value

    # Properties

    @property
    def percent(self) -> float:
        return self.current / self.maximum

    @property
    def maximum(self) -> int:
        return self._maximum

    @maximum.setter
    def maximum(self, value:int):
        """
        Change the maximum value of the gauge.
        If the maximum is geater than the current value, set the current to maximum.
        """
        
        self._maximum = value
        if self.current > self._maximum:
            self.current = self._maximum
            self.changed.emit()  # FIXME: Is is ok?

    # Methods

    def refill(self):
        """Set the current value to its maximum."""
        
        self.current = self.maximum
        self.changed.emit()

    def empty(self):
        """Set the current value to its minimum."""
        
        self.current = 0
        self.changed.emit()

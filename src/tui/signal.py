class Signal:
    """
    Represent a signal that triggers when some actions are played.
    """
    
    def __init__(self):
        self.funcs = list()

    def connect(self, func):
        """Connect a function to this signal.

        The function is executed when the signal emits.
        """

        self.funcs.append(func)

    def disconnect(self, func):
        """Disconnect a previously connected function to this signal."""

        self.funcs.remove(func)

    def disconnect_all(self):
        """Disconnect all the functions connected to this signal."""

        self.funcs.clear()

    def emit(self, *args, **kwargs):
        """Execute all the functions connected to this signal.

        The args and keyword args are given to the function call.
        """
        
        for func in self.funcs:
            func(*args, **kwargs)

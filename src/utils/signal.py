class Signal:
    """
    Represent a signal that triggers when some actions are played.
    """
    
    def __init__(self):
        self.funcs = list()

    def connect(self, func):
        self.funcs.append(fuc)

    def disconnect(self, func):
        self.funcs.remove(func)

    def disconnect_all(self):
        self.funcs.clear()

    def emit(self, *args, **kwargs):
        for func in self.funcs:
            func(*args, **kwargs)

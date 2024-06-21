import copy


class Augment:
    def __init__(self, iid:int):
        self.iid = int(iid)

        self.name = ""
        self.trigger = ""
        self.strenght = 0
        self.resistance = 0

    def __str__(self) -> str:
        return f"Augment({self.name})"

    def __repr__(self) -> str:
        return str(self)

    @classmethod
    def from_dict(cls, iid:int, data:dict):
        augment = cls(iid)
        augment.__dict__.update(data)
        return augment

    def copy(self):
        return copy.deepcopy(self)

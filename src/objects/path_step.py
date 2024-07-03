from src.components import Gauge


class PathStep:
    def __init__(self, iid:int):
        self.iid = int(iid)
        
        self.name = ""
        self.encounters = list()
        self.fountain = Gauge(1)

    def use_fountain(self):
        self.fountain -= 1

    @classmethod
    def from_dict(cls, iid:int, data:dict) -> "PathStep":
        step = cls(iid)
        step.name = data["name"]
        step.fountain.maximum = data["fountains"]
        step.fountain.refill()

        step.encounters = data["encounters"]
        return step

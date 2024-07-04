from src.components import Gauge
from src.objects import Player
import src.singleton as sgt


class PathStep:
    def __init__(self, iid:int):
        self.iid = int(iid)
        
        self.name = ""
        self.fountain = Gauge(1)
        self.encounters_id = list()
        self.encounters = list()

        self.encounter_current = None

    def init(self):
        """
        Initialize the PathStep: fill the fountain and instanciate the encounters.
        """

        self.fountain.refill()
        self.encounters.clear()
        for iid in self.encounters_id:
            self.encounters.append(sgt.encounter_from_id(iid))

    def use_fountain(self):
        self.fountain -= 1

    def select_encounter(self, encounter:Player):
        """
        Select the encounter from its ID.
        """

        index = self.encounters.index(encounter)
        self.encounter_current = self.encounters.pop(index)

    @classmethod
    def from_dict(cls, iid:int, data:dict) -> "PathStep":
        step = cls(iid)
        step.name = data["name"]
        step.fountain.maximum = data["fountains"]
        step.fountain.refill()

        step.encounters_id = data["encounters"]
        return step

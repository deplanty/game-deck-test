import src.singleton as sgt
from src.objects import Player
from src.scenes import SceneCombat


class GameLoop:
    def __init__(self):
        self.current_scene = SceneCombat()

    def start(self):
        self.current_scene.start()


if __name__ == "__main__":
    gm = GameLoop()
    gm.start()

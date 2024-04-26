import src.singleton as sgt
from src.objects import Player
from src.scenes import SceneCombat, SceneSelectEncounter


class GameLoop:
    def __init__(self):
        sgt.root = self
        self.current_scene = SceneSelectEncounter()

    def start(self):
        self.current_scene.start()

    def change_scene(self, scene):
        self.current_scene.stop()
        self.current_scene = scene
        self.current_scene.start()


if __name__ == "__main__":
    gm = GameLoop()
    gm.start()

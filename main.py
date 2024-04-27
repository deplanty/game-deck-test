import src.singleton as sgt
from src.objects import Player
from src.scenes import SceneCombat, SceneSelectEncounter


class GameLoop:
    def __init__(self):
        sgt.root = self
        self.current_scene = SceneSelectEncounter()

    def mainloop(self):
        while True:
            scene = self.current_scene.run()
            if scene:
                self.current_scene = scene
                self.current_scene.run()
            else:
                break
        



if __name__ == "__main__":
    gm = GameLoop()
    gm.mainloop()

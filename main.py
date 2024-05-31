import src.singleton as sgt
from src.objects import Player
from src.scenes import SceneSelectHero


class GameLoop:
    def __init__(self):
        sgt.root = self
        self.current_scene = SceneSelectHero()

    def mainloop(self):
        while self.current_scene:
            scene = self.current_scene.run()
            self.current_scene = scene


if __name__ == "__main__":
    gm = GameLoop()
    gm.mainloop()

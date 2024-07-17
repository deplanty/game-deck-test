#!venv/Scripts/python

import src.singleton as sgt
from src.scenes import SceneMainMenu


class GameLoop:
    def __init__(self):
        sgt.root = self
        self.current_scene = SceneMainMenu()

    def mainloop(self):
        while self.current_scene:
            scene = self.current_scene.run()
            self.current_scene = scene


if __name__ == "__main__":
    gm = GameLoop()
    gm.mainloop()

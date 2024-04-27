import src.singleton as sgt
from src.scenes import Scene, SceneCombat


class SceneSelectEncounter(Scene):
    def run(self):
        """Run this scene loop."""

        super().__init__()
        answer = ""
        scene = None
        while answer != "quit":
            print("List of encounters:")
            for i, encounter in enumerate(sgt.all_encounters, 1):
                print(f"  {i}. {encounter}")
            print("  'quit' to stop.")
            print()
            answer = input("  Input: ")
            if answer.isnumeric():
                answer = int(answer)
                scene = SceneCombat()
                answer = "quit"
        return scene
           

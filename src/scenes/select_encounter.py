import src.singleton as sgt
from src.scenes import Scene, SceneCombat


class SceneSelectEncounter(Scene):
    def __init__(self):
        super().__init__()

        self.encounters = sgt.all_encounters
        
    def run(self):
        """Run this scene loop."""

        answer = ""
        scene = None
        while answer != "quit":
            print("List of encounters:")
            for i, encounter in enumerate(self.encounters):
                print(f"  {i}. {encounter}")
            print("  'quit' to stop.")
            print()
            answer = self.ask_input("  Selection: ")
            if isinstance(answer, int):
                selected = self.encounters[answer]
                scene = SceneCombat(selected.name)
                answer = "quit"
        return scene

    def ask_input(self, text:str) -> int|str:
        answer = input(text)
        if answer.isnumeric():
            answer = int(answer)
        return answer
           

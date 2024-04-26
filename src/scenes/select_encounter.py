import src.singleton as sgt
from src.scenes import SceneCombat


class SceneSelectEncounter:
    def __init__(self):
        self.active = True
        
    def start(self):
        """Mainloop"""

        answer = ""
        while answer != "quit" and self.active:
            print("List of encounters:")
            for i, encounter in enumerate(sgt.all_encounters, 1):
                print(f"  {i}. {encounter}")
            print("  'quit' to stop.")
            print()
            answer = input("  Input: ")
            if answer.isnumeric():
                answer = int(answer)
                sgt.root.change_scene(SceneCombat())
        return 
            
    def stop(self):
        """Stop the mainloop"""

        self.active = False

import src.singleton as sgt
from src.objects import Player


class GameLoop:
    def __init__(self):
        self.player = sgt.encounter_from_name("Lisa")
        self.enemy = sgt.encounter_from_name("number_one")

    def loop_main(self):
        self.player.deck.reform_and_shuffle()
        self.player.start_of_turn()
        while self.player.is_alive() and self.enemy.is_alive():
            action = self.loop_turn()
            if action == "end of turn":
                self.player.start_of_turn()

        if not self.player.is_alive():
            print("DEFEAT")
        else:
            print("VICTORY")

    def loop_turn(self) -> str:
        print("Player:", self.player.info)
        print("Enemy:", self.enemy.info)
        print("")
        print("  Hand:", self.player.deck.hand)
        print(f"  [0-{len(self.player.deck.hand) - 1}] or 'e' to end turn")
        action = self.ask_action("  Pick card: ")
        if isinstance(action, int):
            card = self.player.play_card(action)
            self.enemy.get_hit(card)
            print("  Play card:", card)
            print("            ", card.info)
            print()
            return "continue"
        else:
            return "end of turn"
        
    def ask_action(self, text:str) -> int|str:
        """Ask an action to the user until the answer is valid."""
        
        action = input(text)
        if action.isnumeric():
            return int(action)
        else:
            return action
                


gm = GameLoop()
gm.loop_main()

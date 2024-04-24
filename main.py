import src.singleton as sgt
from src.objects import Player


class GameLoop:
    def __init__(self):
        self.player = sgt.encounter_from_name("Lisa")
        self.enemy = sgt.encounter_from_name("number_one")

    def loop_main(self):
        self.player.deck.reform_and_shuffle()
        self.enemy.deck.reform_and_shuffle()
        turn = "player"
        self.player.start_of_turn()
        while self.player.is_alive() and self.enemy.is_alive():
            if turn == "player":
                action = self.loop_turn()
                if action == "end of turn":
                    turn = "enemy"
                    self.enemy.start_of_turn()
                elif action == "quit":
                    return
            elif turn == "enemy":
                action = self.loop_turn_enemy()
                if action == "end of turn":
                    turn = "player"
                    self.player.start_of_turn() 
                    

        if not self.player.is_alive():
            print("DEFEAT")
        else:
            print("VICTORY")

    def loop_turn(self) -> str:
        print("Player:", self.player.info)
        print("Enemy:", self.enemy.info)
        print()
        print("  Hand:", self.player.deck.hand)
        print(f"  [0-{len(self.player.deck.hand) - 1}] or 'e' to end turn")
        action = self.ask_action("  Pick card: ")
        if isinstance(action, int):
            card = self.player.play_card(action)
            if card is None:
                return "continue"
            self.player.get_buff(card)
            self.enemy.get_hit(card)
            print("  Play card:", card)
            print("            ", card.info)
            print()
            return "continue"
        elif action == "e":
            print("  End of turn")
            print()
            return "end of turn"
        elif action == "q":
            return "quit"
        else:
            print()
            return "continue"

    def loop_turn_enemy(self) -> str:
        print("Enemy:", self.enemy.info)
        print("Player:", self.player.info)
        print()
        card = self.enemy.play_card(0)
        if card is None:
            print("  End of turn")
            print()
            return "end of turn"
        else:
            self.enemy.get_buff(card)
            self.player.get_hit(card)
            print("  Play card:", card)
            print("            ", card.info)
            print()
            return "continue"
        
    def ask_action(self, text:str) -> int|str:
        """Ask an action to the user until the answer is valid."""
        
        action = input(text)
        if action.isnumeric():
            return int(action)
        else:
            return action
                


gm = GameLoop()
gm.loop_main()

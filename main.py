import src.singleton as sgt
from src.objects import Player


class GameLoop:
    def __init__(self):
        self.player = sgt.encounter_from_name("Lisa")
        self.enemy = sgt.encounter_from_name("number_one")

    def loop_main(self):
        self.player.deck.reform_and_shuffle()
        while self.player.is_alive() and self.enemy.is_alive():
            self.player.start_of_turn()
            self.loop_turn()

        if not self.player.is_alive():
            print("DEFEAT")
        else:
            print("VICTORY")

    def loop_turn(self):
        print("Player:", self.player.info)
        print("Enemy:", self.enemy.info)
        print("")
        print("  Hand:", self.player.deck.hand)
        number = self.ask_number("  Pick card: ")
        card = self.player.play_card(number)
        self.enemy.get_hit(card)
        print("  Play card:", card)
        print("            ", card.info)
        print()
        
    def ask_number(self, text:str) -> int:
        """Ask a number to the user until the answer is valid."""
        
        ask = True
        while ask:
            try:
                number = int(input(text))
            except:
                pass
            else:
                ask = False
        return number


gm = GameLoop()
gm.loop_main()

import src.singleton as sgt
from src.scenes import Scene


class SceneCombat(Scene):
    def __init__(self):
        super().__init__()
        self.player = sgt.encounter_from_name("Lisa")
        self.enemy = sgt.encounter_from_name("number_one")

    def run(self):
        """Run this scene loop."""

        self.player.deck.reform_and_shuffle()
        self.enemy.deck.reform_and_shuffle()
        turn = "player"
        self.player.start_of_turn()
        while self.player.is_alive() and self.enemy.is_alive():
            if turn == "player":
                action = self.loop_turn()
                if action == "end of turn":
                    turn = "enemy"
                    self.player.end_of_turn()
                    self.enemy.start_of_turn()
                elif action == "quit":
                    return
            elif turn == "enemy":
                action = self.loop_turn_enemy()
                if action == "end of turn":
                    turn = "player"
                    self.enemy.end_of_turn()
                    self.player.start_of_turn()

        if not self.player.is_alive():
            print("DEFEAT")
        else:
            print("VICTORY")

    def loop_turn(self) -> str:
        """
        The loop controlling the user's turn.

        Returns:
            str: Status after a loop - "continue" or "end of turn".
        """

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
        """
        The loop controlling the enemy's turn.

        Returns:
            str: Status after a loop - "continue" or "end of turn".
        """

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
        """
        Ask an action to the user.

        Args:
            text (str): The text displayed.

        Returns:
            int|str: The user's answer.
        """

        action = input(text)
        if action.isnumeric():
            return int(action)
        else:
            return action

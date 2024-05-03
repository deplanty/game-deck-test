import src.singleton as sgt
from src.scenes import Scene

from .combat_ui import SceneCombatUi


class SceneCombat(Scene):
    def __init__(self, enemy_name:str):
        super().__init__()

        self.enemy = sgt.encounter_from_name(enemy_name)
        self.history_cards = list()

        self.ui = SceneCombatUi(self)

    def run(self):
        """Run this scene loop."""

        sgt.player.deck.reform_and_shuffle()
        self.enemy.deck.reform_and_shuffle()
        turn = "player"
        sgt.player.start_of_turn()
        count = 1
        while sgt.player.is_alive() and self.enemy.is_alive():
            if turn == "player":
                action = self.loop_turn()
                if action == "end of turn":
                    turn = "enemy"
                    sgt.player.end_of_turn()
                    self.enemy.start_of_turn()
                elif action == "quit":
                    return
            elif turn == "enemy":
                action = self.loop_turn_enemy()
                if action == "end of turn":
                    turn = "player"
                    self.enemy.end_of_turn()
                    sgt.player.start_of_turn()

            count += 1

        if not sgt.player.is_alive():
            print("DEFEAT")
        else:
            print("VICTORY")

    def loop_turn(self) -> str:
        """
        The loop controlling the user's turn.

        Returns:
            str: Status after a loop - "continue" or "end of turn".
        """

        self.ui.value_status.text = "Player turn"
        self.ui.update()
        action = self.ask_action()
        self.ui.entry_input.text = ""
        if isinstance(action, int):
            card = sgt.player.play_card(action)
            if card is None:
                return "continue"

            self.play_card(sgt.player, self.enemy, card)
            return "continue"
        elif action == "e":
            return "end of turn"
        elif action == "quit":
            return "quit"
        else:
            return "continue"

    def loop_turn_enemy(self) -> str:
        """
        The loop controlling the enemy's turn.

        Returns:
            str: Status after a loop - "continue" or "end of turn".
        """

        self.ui.value_status.text = "Enemy turn"

        self.ui.update()
        card = self.enemy.play_card(0)
        if card is None:
            return "end of turn"
        else:
            self.play_card(self.enemy, sgt.player, card)
            return "continue"

    def ask_action(self) -> int|str:
        """
        Ask an action to the user.

        Returns:
            int|str: The user's answer.
        """

        action = self.ui.entry_input.text
        if action.isnumeric():
            return int(action)
        else:
            return action

    def play_card(self, source, destination, card):
        source.get_buff(card)
        destination.get_hit(card)
        self.history_cards.append((source, card.copy()))
        self.ui.card_played(source, card)

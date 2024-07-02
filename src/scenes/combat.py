import time

import src.singleton as sgt
from src import scenes

from .combat_ui import SceneCombatUi


class SceneCombat(scenes.Scene):
    def __init__(self, enemy_name:str):
        super().__init__()

        self.enemy = sgt.encounter_from_name(enemy_name)
        self.history_cards = list()

        self.ui = SceneCombatUi(self)
        self.ui.choice_hand.hovered.connect(self._on_player_card_hovered)

    def run(self):
        """Run this scene loop."""

        for i in range(len(sgt.all_augments)):
            sgt.player.add_augment_from_id(i)

        sgt.player.start_of_combat()
        self.enemy.start_of_combat()

        turn = "player"
        sgt.player.start_of_turn()
        count = 1
        while sgt.player.is_alive() and self.enemy.is_alive():
            if turn == "player":
                action = self.loop_turn()
                if action == "end of turn":
                    turn = "enemy"
                    self.ui.choice_hand.focus_remove()
                    sgt.player.end_of_turn()
                    self.enemy.start_of_turn()
                elif action == "quit":
                    return scenes.SceneMainMenu()
            elif turn == "enemy":
                action = self.loop_turn_enemy()
                if action == "end of turn":
                    turn = "player"
                    self.enemy.end_of_turn()
                    sgt.player.start_of_turn()

            count += 1

        sgt.player.end_of_combat()
        self.enemy.end_of_combat()
        if not sgt.player.is_alive():
            return scenes.SceneCombatEnd("defeat")
        else:
            return scenes.SceneCombatEnd("victory")

    def loop_turn(self) -> str:
        """
        The loop controlling the user's turn.

        Returns:
            str: Status after a loop - "continue" or "end of turn".
        """

        self.ui.choice_hand.focus_set()
        self.ui.update()

        index = self.ui.choice_hand.current
        text = self.ui.choice_hand.choice

        if text == "End of turn":
            return "end of turn"
        elif text == "Quit":
            return "quit"
        else:
            card = sgt.player.play_card(index)
            if card is None:
                return "continue"

            self.play_card(sgt.player, self.enemy, card)
            return "continue"

    def loop_turn_enemy(self) -> str:
        """
        The loop controlling the enemy's turn.

        Returns:
            str: Status after a loop - "continue" or "end of turn".
        """

        self.ui.update()
        card = self.enemy.play_card(0)
        if card is None:
            return "end of turn"
        else:
            self.play_card(self.enemy, sgt.player, card)
            time.sleep(0.2)
            return "continue"

    def play_card(self, source, destination, card):
        source.get_buff(card)
        destination.get_hit(card)
        self.history_cards.append((source, card.copy()))
        self.ui.card_played(source, card)

    # Events

    def _on_player_card_hovered(self):
        index = self.ui.choice_hand.current
        if index < len(sgt.player.deck.hand):
            card = sgt.player.deck.hand[index]
            self.ui.label_card_hand.text = card.info_full
        else:
            self.ui.label_card_hand.text = ""
        self.ui.label_card_hand.update()

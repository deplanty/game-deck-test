import time

import src.singleton as sgt
from src import scenes

from .combat_ui import SceneCombatUi


class SceneCombat(scenes.Scene):
    def __init__(self):
        super().__init__()

        self.enemy = sgt.path_step_current.encounter_current
        self.history_cards = list()

        self.ui = SceneCombatUi(self)
        self.ui.choice_hand.hovered.connect(self._on_player_card_hovered)
        self.ui.choice_hand.selected.connect(self._on_player_card_selected)
        self.ui.button_turn_end.pressed.connect(self._on_button_turn_end_pressed)
        self.ui.button_quit.pressed.connect(self._on_button_quit_pressed)

    def run(self):
        """Run this scene loop."""

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
                    self.ui.main.focus_widget.focus_remove()
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
        self.action = ""
        while self.action == "":
            self.ui.update()

        return self.action

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

    def _on_player_card_selected(self):
        index = self.ui.choice_hand.current
        card = sgt.player.play_card(index)
        if card is None:
            self.action = "continue"
            return

        self.play_card(sgt.player, self.enemy, card)
        self.action = "continue"

    def _on_button_turn_end_pressed(self):
        self.action = "end of turn"

    def _on_button_quit_pressed(self):
        self.action = "quit"

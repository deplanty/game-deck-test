import src.singleton as sgt
from src.scenes import Scene
from src import tui


class SceneCombatUi(tui.Tui):
    def __init__(self, scene:Scene):
        super().__init__()
        self.scene = scene

        # Enemy frame with all its compile
        self.frame_enemy = tui.Frame(self)
        self.frame_enemy.grid(0)
        self.label_enemy = tui.Label(self.frame_enemy)
        self.label_enemy.grid(0)
        self.label_enemy_card = tui.Label(self.frame_enemy)
        self.label_enemy_card.grid(1)

        self.frame_player = tui.Frame(self)
        self.frame_player.grid(2)
        self.label_player = tui.Label(self.frame_player)
        self.label_player.grid(0)
        self.label_player_card = tui.Label(self.frame_player)
        self.label_player_card.grid(1)

        self.frame_cards = tui.Frame(self)
        self.frame_cards.grid(3)
        self.label_hand = tui.Label(self.frame_cards)
        self.label_hand.grid(0)

        self.frame_input = tui.Frame(self)
        self.frame_input.grid(4)
        self.label_input = tui.Label(self.frame_input, "Input:")
        self.label_input.grid(0, 0)
        self.entry_input = tui.Entry(self.frame_input)
        self.entry_input.focus_set()
        self.entry_input.grid(0, 1)
        self.label_status = tui.Label(self.frame_input, "Status:")
        self.label_status.grid(1, 0)
        self.value_status = tui.Label(self.frame_input)
        self.value_status.grid(1, 1)
        
        self.update()

    def update(self):
        self.label_enemy.text = self.scene.enemy.info
        self.label_player.text = sgt.player.info
        self.label_hand.text = sgt.player.deck.hand
        super().update()

    def card_played(self, player, card):
        label = {
            self.scene.enemy: self.label_enemy_card,
            sgt.player: self.label_player_card
        }.get(player)

        label.text = f"{card}\n{card.info}"

        
class SceneCombat(Scene):
    def __init__(self, enemy_name:str):
        super().__init__()
        self.enemy = sgt.encounter_from_name(enemy_name)

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

        # print("Player:", sgt.player.info)
        # print("Enemy:", self.enemy.info)
        # print()
        # print("  Hand:", sgt.player.deck.hand)
        # print(f"  [0-{len(sgt.player.deck.hand) - 1}] or 'e' to end turn")
        # action = self.ask_action("  Pick card: ")
        self.ui.value_status.text = "Player turn"
        self.ui.update()
        action = self.ask_action()
        self.ui.entry_input.text = ""
        if isinstance(action, int):
            card = sgt.player.play_card(action)
            if card is None:
                return "continue"
            sgt.player.get_buff(card)
            self.enemy.get_hit(card)
            self.ui.card_played(sgt.player, card)
            # print("  Play card:", card)
            # print("            ", card.info)
            # print()
            return "continue"
        elif action == "e":
            # print("  End of turn")
            # print()
            return "end of turn"
        elif action == "quit":
            return "quit"
        else:
            # print()
            return "continue"

    def loop_turn_enemy(self) -> str:
        """
        The loop controlling the enemy's turn.

        Returns:
            str: Status after a loop - "continue" or "end of turn".
        """

        self.ui.value_status.text = "Enemy turn"

        # print("Enemy:", self.enemy.info)
        # print("Player:", sgt.player.info)
        # print()
        self.ui.update()
        card = self.enemy.play_card(0)
        if card is None:
            # print("  End of turn")
            # print()
            return "end of turn"
        else:
            self.enemy.get_buff(card)
            sgt.player.get_hit(card)
            self.ui.card_played(self.enemy, card)
            # print("  Play card:", card)
            # print("            ", card.info)
            # print()
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

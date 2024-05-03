import src.singleton as sgt
from src.scenes import Scene
from src import tui


class SceneCombatUi(tui.Tui):
    def __init__(self, scene:Scene):
        super().__init__()
        self.scene = scene

        # Enemy frame
        self.frame_enemy = tui.Frame(self)
        self.frame_enemy.grid(0, columnspan=2)
        self.label_enemy_name = tui.Label(self.frame_enemy, align="center")
        self.label_enemy_name.grid(0)
        self.enemy_hp = tui.Progressbar(self.frame_enemy, align="center")
        self.enemy_hp.grid(1)
        self.label_enemy_info = tui.Label(self.frame_enemy)
        self.label_enemy_info.grid(2)
        self.label_enemy_card = tui.Label(self.frame_enemy)
        self.label_enemy_card.grid(3)

        # Player frame
        self.frame_player = tui.Frame(self)
        self.frame_player.grid(1, columnspan=2)
        self.label_player_name = tui.Label(self.frame_player, align="center")
        self.label_player_name.grid(0)
        self.player_hp = tui.Progressbar(self.frame_player, align="center")
        self.player_hp.grid(1)
        self.label_player_info = tui.Label(self.frame_player)
        self.label_player_info.grid(2)
        self.label_player_card = tui.Label(self.frame_player)
        self.label_player_card.grid(3)

        # History of played cards
        self.frame_history = tui.Label(self)
        self.frame_history.filler = "."
        self.frame_history.grid(0, 2, rowspan=3)

        # Cards in player's hand frame
        self.frame_cards = tui.Frame(self)
        self.frame_cards.grid(2, columnspan=3)
        self.label_hand = tui.Label(self.frame_cards)
        self.label_hand.grid(0)

        # Frame for the user inputs
        self.frame_input = tui.Frame(self)
        self.frame_input.grid(3, columnspan=3)
        self.label_input = tui.Label(self.frame_input)
        self.label_input.grid(0, 0)
        self.entry_input = tui.Entry(self.frame_input)
        self.entry_input.focus_set()
        self.entry_input.grid(0, 1)
        self.label_status = tui.Label(self.frame_input)
        self.label_status.grid(1, 0)
        self.value_status = tui.Label(self.frame_input)
        self.value_status.grid(1, 1)

        # Initialize values
        self.label_enemy_name.text = self.scene.enemy.name
        self.enemy_hp.maximum = self.scene.enemy.health.maximum
        self.label_player_name.text = sgt.player.name
        self.player_hp.maximum = sgt.player.health.maximum
        self.label_input.text = "Input:\n  n - Card number\n  e - End of turn\n  quit - Quit game"
        self.label_status.text = "Status:"

    def update(self):
        # Update player and enemy health and all
        self.label_enemy_info.text = self.scene.enemy.info
        self.enemy_hp.current = self.scene.enemy.health.current
        self.label_player_info.text = sgt.player.info
        self.player_hp.current = sgt.player.health.current

        # Show the cards in hand
        cards = ["Cards in hand:"]
        for i, card in enumerate(sgt.player.deck.hand):
            cards.append(f"   {i}. {card} - {card.info}")
        self.label_hand.text = "\n".join(cards)

        # Show the history of played cards
        history = list()
        for player, card in self.scene.history_cards:
            history.insert(0, f"{player.name}: {card}")
        self.frame_history.text = "\n".join(history)
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

            self.play_card(sgt.player, self.enemy, card)
            # sgt.player.get_buff(card)
            # self.enemy.get_hit(card)
            # self.ui.card_played(sgt.player, card)
            # self.history_cards.append((sgt.player, card.copy()))
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
            self.play_card(self.enemy, sgt.player, card)
            # self.enemy.get_buff(card)
            # sgt.player.get_hit(card)
            # self.ui.card_played(self.enemy, card)
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

    def play_card(self, source, destination, card):
        source.get_buff(card)
        destination.get_hit(card)
        self.history_cards.append((source, card.copy()))
        self.ui.card_played(source, card)

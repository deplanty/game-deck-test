import src.singleton as sgt
from src import tui


class SceneCombatUi(tui.Tui):
    def __init__(self, scene):
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

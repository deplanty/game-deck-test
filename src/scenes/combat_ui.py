import src.singleton as sgt
from src import tui
from src.tui.style import Style


class SceneCombatUi(tui.Tui):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene

        # Enemy frame
        self.frame_enemy = tui.Frame(self)
        self.frame_enemy.grid(0, columnspan=2)
        self.label_enemy_name = tui.Label(self.frame_enemy, align="center", style=Style.TEXT_PRIMARY)
        self.label_enemy_name.pack()
        self.enemy_hp = tui.Progressbar(self.frame_enemy, align="center", style=Style.TEXT_DANGER)
        self.enemy_hp.pack()
        frame = tui.Frame(self.frame_enemy)
        frame.pack()
        self.label_enemy_info = tui.Label(frame)
        self.label_enemy_info.grid(0, 0)
        self.label_enemy_card = tui.Label(frame)
        self.label_enemy_card.grid(0, 1)

        # Player frame
        self.frame_player = tui.Frame(self)
        self.frame_player.grid(1, columnspan=2)
        self.label_player_name = tui.Label(self.frame_player, align="center", style=Style.TEXT_PRIMARY)
        self.label_player_name.pack()
        self.player_hp = tui.Progressbar(self.frame_player, align="center", style=Style.TEXT_DANGER)
        self.player_hp.pack()
        frame = tui.Frame(self.frame_player)
        frame.pack()
        self.label_player_info = tui.Label(frame)
        self.label_player_info.grid(0, 0)
        self.label_player_card = tui.Label(frame)
        self.label_player_card.grid(0, 1)

        # History of played cards
        self.frame_history = tui.Label(self)
        self.frame_history.filler = "."
        self.frame_history.grid(0, 2, rowspan=2)

        # Cards in player's hand frame
        self.frame_cards = tui.Frame(self)
        self.frame_cards.grid(2, columnspan=3)
        self.choice_hand = tui.Choice(self.frame_cards)
        self.choice_hand.grid(0, 0)
        self.label_card_hand = tui.Label(self.frame_cards)
        self.label_card_hand.prefix = "Hovered card:\n"
        self.label_card_hand.grid(0, 1, columnspan=3)

        # Frame for the user inputs
        self.frame_input = tui.Frame(self)
        self.frame_input.grid(3, columnspan=3)
        self.label_status = tui.Label(self.frame_input)
        self.label_status.pack()

        # Initialize values
        self.label_enemy_name.text = self.scene.enemy.name
        self.enemy_hp.maximum = self.scene.enemy.health.maximum
        self.label_player_name.text = sgt.player.name
        self.player_hp.maximum = sgt.player.health.maximum
        self.label_status.prefix = "Status: "

    def update(self):
        # Update player and enemy health and all
        self.label_enemy_info.text = self.scene.enemy.info
        self.enemy_hp.current = self.scene.enemy.health.current
        self.label_player_info.text = sgt.player.info
        self.player_hp.current = sgt.player.health.current

        # Show the cards in hand
        cards = ["Cards in hand:"]
        self.choice_hand.reset_choices()
        for i, card in enumerate(sgt.player.deck.hand):
            if sgt.player.energy >= card.cost:
                style = Style.NORMAL
            else:
                style = Style.MUTE
            self.choice_hand.add_label(card.name_full, style=style)
        self.choice_hand.add_label("End of turn", style=Style.TEXT_INFO)
        self.choice_hand.add_label("Quit", style=Style.TEXT_WARNING)
        self.frame_cards.fill()

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

from src.components import Health, Gauge
from src.objects import Card, Deck
import src.singleton as sgt


class Player:
    """
    Create a player.

    Args:
        name (str): The player's name.
        max_health (int): The player's max health.
    """
    
    def __init__(self, name:str, max_health:int):
        self.name = name
        self.health = Gauge(max_health)
        self.deck = Deck()
        self.energy = Gauge(4)
        self.hand_size = 2
        # Buffs
        self.armor = 0

    def __str__(self) -> str:
        return f"Player({self.name}, {self.health})"

    # Properties
    
    @property
    def info(self) -> str:
        """Returns the information of the player"""
        
        text = f"{str(self)}\n"
        text += f"Deck = {self.deck.info}\n"
        text += f"Armor = {self.armor}"
        return text

    # Class methods

    @classmethod
    def from_dict(cls, name:str, data:dict):
        """
        Return a player with all its data from a dict.

        Args:
            name (str): The player's name.
            data (dict): All the data needed.

        Returns:
            Player: The build player from dict.
        """

        player = Player(name, data["hp"])
        player.energy.maximum = data["energy"]
        player.hand_size = data["hand_size"]
        for iid in data["deck"]:
            card = sgt.card_from_id(iid)
            player.deck.add(card)
        return player
    
    # Method

    def start_of_turn(self):
        """
        Make all the action at the start of the turn:
        discard hand, draw new hand, reset armor.
        """

        self.deck.discard_hand()
        self.deck.draw(self.hand_size)
        self.armor = 0
        self.energy.refill()

    def play_card(self, index:int) -> Card:
        """
        Play the card given by its index.
        If the player doesn't have enough energy, return None.

        Args:
            index (int): index of the card in the hand.

        Returns:
            Card: The card being played.
        """

        card = self.deck.hand[index]
        if self.energy < card.cost:
            return None

        self.energy -= card.cost
        return self.deck.play_from_hand(index)
        
    def get_hit(self, card:Card):
        """
        The player gets hit by a card and apply the effect of the card.

        Args:
            card (Card): The card applying its effects on the player.
        """

        # The card deal damage to the armor. If the armor drops to 0, damage the player.
        if card.damage >= self.armor:
            damage = card.damage - self.armor
            self.armor = 0
            self.health -= damage
        else:
            self.armor -= card.damage

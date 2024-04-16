from src.components import Health
from src.objects import Card, Deck


class Player:
    """
    Create a player.

    Args:
        name (str): The player's name.
    """
    
    def __init__(self, name:str, max_health:int):
        self.name = name
        self.health = Health(max_health)
        self.deck = Deck()
        self.energy = 2
        self.hand_size = 2
        # Buffs
        self.armor = 0

    def __str__(self) -> str:
        return f"Player({self.name}, {self.health})"

    # Method

    @property
    def info(self) -> str:
        """Returns the information of the player"""
        
        text = f"{str(self)}\n"
        text += f"Armor = {self.armor}"
        return text

    def draw_hand(self):
        """Draw a hand."""
        self.deck.draw(self.hand_size)

    def play_card(self, index:int) -> Card:
        """
        Play the card given by its index.

        Args:
            index (int): index of the card in the hand.

        Returns:
            Card: The card being played.
        """

        return self.deck.hand.pop(index)
        
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

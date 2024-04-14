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

    def __str__(self) -> str:
        return f"Player({self.name}, {self.health})"

    # Method

    def draw_hand(self):
        """Draw a hand."""
        self.deck.draw(self.hand_size)

    def play_card(self, index:int) -> Card:
        """
        Play the card given by its index.

        Args:
            index (int): index of the card in the hand.
        """

        return self.deck.hand.pop(index)
        

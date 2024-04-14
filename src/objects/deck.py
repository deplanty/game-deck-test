import random
import typing

from src.objects import Card
    

class Deck:
    """
    Create a deck. Stores the cards of the player.
    The `deck` contains the cards that can be drawn.
    The `discard` contains the cards that have been played or discarded.
    The `exile` contains the cards that can't be played anymore.
    The `hand` contains the cards currently in the hand of the player.
    """
    
    def __init__(self):
        self.deck = list()
        self.discard = list()
        self.exile = list()
        self.hand = list()

    def __str__(self):
        return str(self.deck)

    # Methods
    
    def add_new(self, card:Card):
        """
        Add a new card to the deck by copying it.

        Args:
            card (Card): The card to add to the deck.
        """
        
        self.deck.append(card.copy())

    def prepare(self):
        """Reform the deck by adding the discarded and exiled cards."""
        
        self.deck.extend(self.discard)
        self.discard.clear()
        self.deck.extend(self.exile)
        self.exile.clear()
        self.deck.extend(self.hand)
        self.hand.clear()

    def shuffle(self):
        """Shuffle all the cards without the hand into the deck."""
        
        self.deck.extend(self.discard)
        self.discard.clear()
        self.deck.extend(self.exile)
        self.exile.clear()
        random.shuffle(self.deck)

    def reset(self):
        """Clear the deck of all its cards."""
        
        self.deck.clear()
        self.discard.clear()
        self.exile.clear()

    def draw(self, n_cards:int):
        """
        Draw a certain amount of cards to the hand of the player.

        Args:
            n_cards (int): Number of cards to be drawn.
        """

        for _ in range(n_cards):
            self.hand.append(self.deck.pop(-1))

            if len(self.deck) == 0:
                self.shuffle()

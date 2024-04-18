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

    # Properties

    @property
    def info(self) -> str:
        text = f"{len(self.deck)} in deck, {len(self.discard)} in discard"
        return text
    
    # Methods
    
    def add(self, card:Card):
        """
        Add a card to the deck.

        Args:
            card (Card): The card to add to the deck.
        """
        
        self.deck.append(card)

    def play_from_hand(self, index:int) -> Card:
        """
        Play a card in hand.

        Args:
            index (int): The index of the card in the hand.

        Returns:
            Card: The card played.
        """

        card = self.hand.pop(index)
        self.discard.append(card)
        return card
        
    def reform(self):
        """Reform the deck by adding all the cards (discarded, exiled and in hand) in the deck."""
        
        self.deck.extend(self.discard)
        self.discard.clear()
        self.deck.extend(self.exile)
        self.exile.clear()
        self.deck.extend(self.hand)
        self.hand.clear()

    def shuffle_deck(self):
        """Shuffle the cards in the deck."""

        random.shuffle(self.deck)

    def reform_and_shuffle(self):
        """Reform the deck and shuffle all the cards."""

        self.reform()
        self.shuffle_deck()

    def discard_hand(self):
        """Put cards in hand into the discard pile."""

        self.discard.extend(self.hand)
        self.hand.clear()

    def shuffle_discard_in_deck(self):
        """Add all the discarded cards into the deck and shuffle."""
        
        self.deck.extend(self.discard)
        self.discard.clear()
        self.shuffle_deck()

    def clear(self):
        """Clear the deck of all its cards."""
        
        self.deck.clear()
        self.discard.clear()
        self.exile.clear()

    def _draw(self):
        """Draw a card and add it into the deck."""
        
        self.hand.append(self.deck.pop(0))
        
    def draw(self, n_cards:int):
        """
        Draw a certain amount of cards to the hand of the player.
        If the deck is depleted before all cards are drawn, shuffle the discarded cards
        into the deck.
        TODO: If the deck is still empty, it means that all the cards are in the hand.

        Args:
            n_cards (int): Number of cards to be drawn.
        """

        # If the player wants to draw a card but the deck is empty, then shuffle the discarded cards
        # in the deck. If the deck is still empty, it means that all the cards are in the hand.
        
        for _ in range(n_cards):
            if len(self.deck) == 0:
                print("DECK EMPTY RESHUFFLE")
                self.shuffle_discard_in_deck()

            self._draw()

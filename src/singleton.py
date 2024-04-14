import toml

from src.objects import Card


# Register all the cards in the game.
#  They are stored in a dict {iid: card}.
all_cards = dict()
for name, data in toml.load("resources/cards.toml").items():
    card = Card.from_dict(name, data)
    all_cards[card.iid] = card

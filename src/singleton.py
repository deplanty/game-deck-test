import toml

from src.objects import Card, Player


def card_from_id(iid:int, copy:bool=True) -> Card:
    """
    Return the card given by its ID.
    If `copy` is true, copy the card.

    Args:
        iid (int): The card ID.
        copy (bool): Copy or not the returned card.

    Returns:
        Card: The card wanted.
    """

    card = all_cards[iid]
    if copy:
        return card.copy()
    else:
        return card

# Register all the cards in the game.
#  They are stored in a dict {id: card}.
all_cards = dict()
for name, data in toml.load("resources/cards.toml").items():
    card = Card.from_dict(name, data)
    all_cards[card.iid] = card

# Register all the players in the game.
#  They are stored in a dict {name: player}
all_players = dict()
for name, data in toml.load("resources/encounters.toml").items():
    player = Player.from_dict(name, data)
    all_players[player.name] = player

import random

import toml

from src.objects import Augment, Card, Player


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
    global all_cards

    for card in all_cards:
        if card.iid == iid:
            if copy:
                return card.copy()
            else:
                return card


def get_random_cards(n:int=1) -> list[Card]:
    """
    Return a random number of cards.

    Args:
        n (int): The number of cards returned.

    Returns:
        list[Card]: The list of the cards returned.
    """
    global all_cards

    return random.choices(all_cards, k=n)


def encounter_from_name(name:str, copy:bool=True) -> Player:
    """
    Return the encounter given by its name.
    If `copy` is true, copy the encounter.

    Args:
        name (str): The encounter's name.
        copy (bool): Copy or not the returned encounter.

    Returns:
        Player: The wanted encounter
    """
    global all_encounters

    for enc in all_encounters:
        if enc.name == name:
            if copy:
                return enc.copy()
            else:
                return enc


def augment_from_id(iid:int, copy:bool=True) -> Card:
    """
    Return the augment given by its ID.
    If `copy` is true, copy the augment.

    Args:
        iid (int): The augment ID.
        copy (bool): Copy or not the returned augment.

    Returns:
        Augment: The augment wanted.
    """
    global all_augments

    for augment in all_augments:
        if augment.iid == iid:
            if copy:
                return augment.copy()
            else:
                return augment


# Register all the cards in the game.
#  They are stored in a dict {id: card}.
all_cards = list()
for iid, data in toml.load("resources/cards.toml").items():
    card = Card.from_dict(iid, data)
    all_cards.append(card)

all_augments = list()
for iid, data in toml.load("resources/augments.toml").items():
    augment = Augment.from_dict(iid, data)
    all_augments.append(augment)

# All encounters are stored in a list
all_encounters = list()
for iid, data in toml.load("resources/encounters.toml").items():
    player :Player= Player.from_dict(iid, data)
    all_encounters.append(player)

# All heroes are stored in a list
all_heroes = list()
for iid, data in toml.load("resources/heroes.toml").items():
    player :Player= Player.from_dict(iid, data)
    all_heroes.append(player)

# The tester have access to all the cards
# and all augments
tester :Player= all_heroes[0]
for card in all_cards:
    tester.add_card_from_id(card.iid)
for augment in all_augments:
    tester.add_augment_from_id(augment.iid)

text_victory = """\
 __      ___      _                   
 \ \    / (_)    | |                  
  \ \  / / _  ___| |_ ___  _ __ _   _ 
   \ \/ / | |/ __| __/ _ \| '__| | | |
    \  /  | | (__| || (_) | |  | |_| |
     \/   |_|\___|\__\___/|_|   \__, |
                                 __/ |
                                |___/ 

"""

text_defeat = """\
  _____        __           _   
 |  __ \      / _|         | |  
 | |  | | ___| |_ ___  __ _| |_ 
 | |  | |/ _ \  _/ _ \/ _` | __|
 | |__| |  __/ ||  __/ (_| | |_ 
 |_____/ \___|_| \___|\__,_|\__|

"""


root = None
player = None

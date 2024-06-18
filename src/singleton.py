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
    global all_cards

    card = all_cards[iid]
    if copy:
        return card.copy()
    else:
        return card


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
    global all_players

    encounter = all_players[name]
    if copy:
        return encounter.copy()
    else:
        return encounter


# Register all the cards in the game.
#  They are stored in a dict {id: card}.
all_cards = dict()
for iid, data in toml.load("resources/cards.toml").items():
    card = Card.from_dict(iid, data)
    all_cards[card.iid] = card

# Register all the players in the game.
#  They are stored in a dict {name: player}
all_players = dict()
for iid, data in toml.load("resources/encounters.toml").items():
    player = Player.from_dict(iid, data)
    all_players[player.name] = player

# All encounters are stored in a list
all_encounters = [
    encounter_from_name(name) for name in ["Dumbo", "First One", "First Two", "The Third", "No Pain No Gain"]
]

# All heroes are stored in a list
all_heroes = [
    encounter_from_name(name) for name in ["Tester", "Lisa", "Jacques", "Barnabé"]
]
# The tester have access to all the cards
tester = all_heroes[0]
for card in all_cards:
    tester.add_card_from_id(card)


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

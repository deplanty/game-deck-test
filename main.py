import src.singleton as sgt
from src.objects import Player


# Register all the cards in the game.
#  They are stored in a dict {iid: card}.
# for card in sgt.all_cards.values():
#     print(card._info)
#     print()


player = Player("Lisa", 100)
player.deck.add_new(sgt.all_cards[1])
player.deck.add_new(sgt.all_cards[1])
player.deck.add_new(sgt.all_cards[1])
player.deck.add_new(sgt.all_cards[3])

player.deck.deck[0].upgrade()
player.deck.deck[1].upgrade_multiple(3)
print(player)
print(player.deck)
print()

enemy = Player("Pap's", 40)
enemy.deck.add_new(sgt.all_cards[2])
enemy.deck.add_new(sgt.all_cards[2])
enemy.deck.add_new(sgt.all_cards[2])
print(enemy)
print(enemy.deck)
print()


print("Init deck:", player.deck.deck)
player.deck.reset_and_shuffle()
print("Reset and shuffle:", player.deck.deck)

player.draw_hand()
print("Draw hand 1:", player.deck.hand)

player.draw_hand()
print("Draw hand 2:", player.deck.hand)

player.draw_hand()
print("Draw hand 3:", player.deck.hand)

player.deck.discard_hand()
print("Discard hand")
print("Hand:", player.deck.hand)
print("Discard:", player.deck.discard)

player.deck.shuffle_discard_in_deck()
print("Shuffle discard in deck")
print("Discard:", player.deck.discard)
print("Deck:", player.deck.deck)

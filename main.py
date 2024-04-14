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


player.draw_hand()
print(player.deck.hand)
card = player.play_card(0)
print(card._info)
print(player.deck.hand)

enemy.health -= card.damage
print(enemy)

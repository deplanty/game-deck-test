import src.singleton as sgt
from src.objects import Player


# Register all the cards in the game.
#  They are stored in a dict {iid: card}.
# for card in sgt.all_cards.values():
#     print(card._info)
#     print()


player = Player("Lisa", 100)
player.deck.add(sgt.all_cards[1])
player.deck.add(sgt.all_cards[1])
player.deck.add(sgt.all_cards[1])
player.deck.add(sgt.all_cards[3])

player.deck.deck[0].upgrade()
player.deck.deck[1].upgrade(3)
print("Player:", player)
print(player.deck)
print()

enemy = Player("Pap's", 40)
enemy.armor = 2
print("Enemy:", enemy.info)
print()

player.draw_hand()
card = player.play_card(0)
enemy.get_hit(card)
print(player, "plays", card)
print(card.info)
print("Enemy:", enemy.info)

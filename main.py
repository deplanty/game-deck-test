import src.singleton as sgt
from src.objects import Player


player = sgt.all_players["Lisa"]
enemy = sgt.all_players["number_one"]

print("Player:", player.info)
print("Enemy: ", enemy.info)
print()


player.deck.reform_and_shuffle()

player.start_of_turn()
print("Hand", player.deck.hand)
print()
card = player.play_card(0)
enemy.get_hit(card)
print(card, enemy)
print()
print("Hand", player.deck.hand)

card = player.play_card(0)
enemy.get_hit(card)
print(card, enemy)
print()
print("Hand", player.deck.hand)

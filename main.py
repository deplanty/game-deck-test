import src.singleton as sgt
from src.objects import Player


player = sgt.all_players["Lisa"]
enemy = sgt.all_players["number_one"]

# Start of encounter
player.deck.reform_and_shuffle()

count = 0

while player.health > 0 or enemy.health > 0 or count > 20:
    count += 1
    print("Start of turn", count)
    print("Player:", player.info)
    print("Enemy:", enemy)
    print()
    player.start_of_turn()
    print("    Hand:", player.deck.hand)
    number = int(input("    Pick card: "))
    card = player.play_card(number)
    if card:
        enemy.get_hit(card)
        print("    Play card:", card)
        print("              ", card.info)
        print()
    else:
        print("Card is None")

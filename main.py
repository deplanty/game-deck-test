import src.singleton as sgt
from src.objects import Player


player = sgt.all_players["Lisa"]
enemy = sgt.all_players["number_one"]

print("Player:", player.info)
print("Enemy: ", enemy.info)
print()

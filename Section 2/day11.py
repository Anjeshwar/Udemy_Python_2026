# Lottery program

import random

lottery_numbers = set(random.sample(list(range(22)), 6))

players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},              #players[0]  
    {"name": "Charlie", "numbers": {2, 7, 9, 22, 10, 5}},          #players[1] 
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},         #players[2] 
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},             #players[3] 
]

top_player = players[0]  

for player in players:
    matched_numbers = len(player["numbers"].intersection(lottery_numbers))  
    if matched_numbers > len(top_player["numbers"].intersection(lottery_numbers)):
        top_player = player
        
winnings = 100 ** len(top_player["numbers"].intersection(lottery_numbers))

print(f"{top_player['name']} won {winnings}.")
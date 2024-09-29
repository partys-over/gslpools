#gslpools.py

import random

players = open('players.txt', 'r')
global shuffledplayers
shuffledplayers = []

for line in players:
    print(line[:-1])
    shuffledplayers.append(line.replace('\n', ''))

random.shuffle(shuffledplayers)

print(shuffledplayers)

count = 0
pool = 1

while count < 32:
    print("Pool " + str(pool))
    print('Matchup 1:', shuffledplayers[count], 'vs', shuffledplayers[(count + 1)])
    print('Matchup 2:', shuffledplayers[(count + 2)], 'vs', shuffledplayers[(count + 3)])
    print('Matchup 3: Winner of Matchup 1 vs Winner of Matchup 2 [Winner quals]')
    print('Matchup 4: Loser of Matchup 1 vs Loser of Matchup 2')
    print('Matchup 5: Winner of Matchup 4 vs Loser of Matchup 3 [Winner quals]')
    pool += 1
    count += 4

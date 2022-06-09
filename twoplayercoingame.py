import random

def flip_coin():
    return random.random() < 0.5

def run_game(strat1, strat2):
    last_three = []
    for i in range(3):
        last_three.append(flip_coin())
    winner = 0
    while winner == 0:
        if last_three == strat1:
            winner = 1
        elif last_three == strat2:
            winner = 2
        else:
            last_three.append(flip_coin())
            last_three.pop(0)
    return winner

def run_strats(strat1, strat2):
    count = 0
    for i in range(1000):
        if run_game(strat1, strat2) == 1:
            count += 1
    return count/1000

strats = []
for i in [True, False]:
    for j in [True, False]:
        for k in [True, False]:
            strats.append([i,j,k])

for strat1 in strats:
    for strat2 in strats:
        if strat1 != strat2:
            print(strat1, strat2, run_strats(strat1, strat2))
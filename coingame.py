import random

def flip_coin():
    return random.choice([True, False])

outcomes = [[True, True, True],
            [True, True, False],
            [True, False, True],
            [True, False, False],
            [False, True, True],
            [False, True, False],
            [False, False, True],
            [False, False, False]]

def play_game(player1,player2):
    last_three = []
    for i in range(3):
        last_three.append(flip_coin())
    game_end = False
    while game_end == False:
        if last_three == player1:
            return 1
        elif last_three == player2:
            return 0
        else:
            last_three.append(flip_coin())
            last_three.pop(0)

for i in range(8):
    min = 1
    min_j = 0
    for j in range(8):      
        if i == j:
            continue
        else:
            count = 0
            for k in range(10000):
                count += play_game(outcomes[i],outcomes[j])
            print("Player 1: " + str(i) + " | Player 2: " + str(j) + " | 1 win rate: " + str(count/10000))
            if count/10000 < min:
                min = count/10000
                min_j = j
    print("If player 1 chooses " + str(i) + ", player 2 should choose " + str(min_j) + " then player 1 wins " + str(min) + " of the time.")
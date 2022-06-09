import random

def flip_coin():
    return random.choice([True, False])

total = 0
for i in range(10000):
    last_three = []
    for i in range(2):
        last_three.append(flip_coin())
    if last_three == [False, False]:
        total += 1
        continue
    else:
        last_three.append(flip_coin())
    game_end = False
    while game_end == False:
        if last_three == [True, True, True]:
            game_end = True
        elif last_three[1:3] == [False, False]:
            total += 1
            game_end = True
        else:
            last_three.append(flip_coin())
            last_three.pop(0)
    # print(last_three)
print(total/10000)


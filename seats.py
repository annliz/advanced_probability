import random

n = 100

def run_game():

    seat_taken = [False]*n

    random_seat = random.randint(0,n-1)
    seat_taken[random_seat] = True

    for i in range(1,n-1):
        if not seat_taken[i]:
            seat_taken[i] = True
        else:
            got_seat = False
            while got_seat == False:
                random_seat = random.randint(0,n-1)
                if not seat_taken[random_seat]:
                    seat_taken[random_seat] = True
                    got_seat = True
    
    return not seat_taken[n-1]

count = 0
for i in range(1000):
    if run_game():
        count += 1
print(count)

    


import random

a = 0 # initialize counts of each person being guilty
b = 0

for i in range(100000):
    blood = random.randint(1,10) # select random blood type for the second person
    second_blood = False
    if blood==1:
        second_blood = True # set whether the second person has the given blood type
    choices = [[True, True],[second_blood, False]]
    A = choices.pop(random.randint(0,1)) # randomly assign persons A and B to the two profiles
    B = choices[0]
    if not A[0]:
        continue # if A is not guilty, skip the rest of the loop because it is not within our sample space
    elif A[1]:
        a += 1 # if A is guilty, increment the count of A being guilty
    else:
        b += 1 # else, increment the count of B being guilty

print(a/(a+b)) # print the probability of A being guilty
    
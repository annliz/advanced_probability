import math

def expected_value(r):
    total = 0
    for n in range(1000):
        v = 0
        for k in range(math.floor(r*n)+1,n+1):
            v += math.comb(n,k)*(math.floor(r*n)+1)/n
        v *= 0.5**n
        total += v
    return total

print(expected_value(0.5))


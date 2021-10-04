from functools import reduce

nimbers = []
input()

piles = list(map(int, input().split()))
xor = lambda x: reduce(lambda x, y: x^y, x)
nim_sum = xor(piles)

count = 0
if nim_sum != 0:
    for i in piles:
        if i^nim_sum < i:
            count += 1

print(count)
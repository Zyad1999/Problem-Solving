from collections import Counter
from math import sqrt


def primes(n):
    x = [True] * ((n - 1) // 2)
    for i in range(int((sqrt(n) - 3) // 2) + 1):
        if x[i]:
            x[2 * i * i + 6 * i + 3::2 * i + 3] = [False] * int((n - (2 * i + 3) ** 2) // (4 * i + 6) + 1)
    return [2] + [2 * i + 3 for i, v in enumerate(x) if v]


def middle_out(counts):
    divisor = 10 ** 9 + 7
    count = [0] * 4501
    for i, n in counts:
        count[i] = n
    path = ((4096, 4351), (4352, 4500), (3584, 4095), (3500, 3583))
    span = ((256, 0), (512, 0), (512, 4096), (1024, 4096))

    totals = [[0] * 8192 for _ in range(2)]
    static, update = 0, 1
    totals[static][0] = 1

    for i, p in enumerate(path):
        for j, n in enumerate(count[p[0]:p[1] + 1]):
            if n:
                same = 1 + n // 2

                change = (n + 1) // 2
                o = span[i][1]
                for x in range(span[i][0]):

                    y = x ^ (j + p[0])
                    totals[update][x] = (totals[static][y] * change +
                                         totals[static][x] * same)
                    totals[update][y] = (totals[static][x] * change +
                                         totals[static][y] * same)
                    if o:
                        totals[update][x + o] = (totals[static][y + o] * change +
                                                 totals[static][x + o] * same)
                        totals[update][y + o] = (totals[static][x + o] * change +
                                                 totals[static][y + o] * same)
                if totals[update][0] > 100000 * divisor:
                    for x in range(len(totals[update])):
                        totals[update][x] %= divisor
                static, update = update, static

    p = primes(8191)
    total = 0
    for prime in p:
        total += totals[static][prime]

    return total % divisor


q = int(input())
for _ in range(q):
    n = int(input())
    numbers = Counter(int(x) for x in input().split()).items()
    print(middle_out(numbers))
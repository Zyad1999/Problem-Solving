def lsb(x):
    res = 1
    while not (x & 1):
        x >>= 1
        res <<= 1
    return res

tests = int(input())
for i in range(tests):
    x = int(input())
    answer = lsb(x)
    print(answer)
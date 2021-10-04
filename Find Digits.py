t = int(input())
for i in range(0,t):
    n = input()
    a = list(map(int, n))
    b = int(n)
    c = 0
    for j in a:
        if (j != 0 and b % j == 0):
            c += 1
    print (c)
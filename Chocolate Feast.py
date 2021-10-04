R = int(input())

for i in range(0,R):

    n, c, m = map(int, input().split())
    Chocolates = Papers = n//c

    while Papers >= m:
        k = Papers // m
        Chocolates += k
        Papers += k*(1-m)

    print (Chocolates)
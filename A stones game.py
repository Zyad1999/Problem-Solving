def getGrundy(n):
    if n&1: return 1
    i = n.bit_length()-1
    return i + 2*(i&1)
for _ in range(int(input())):
    n = int(input())
    g = getGrundy(n)
    i = 1 << g.bit_length()-1
    a = 1 << (i-1)
    b = 1 << (i^g)
    res = a-b+1
    least = (a >> 1) + (a & 1)
    #print(); print(g, i); print(least, res)
    if res < least:
        print(least)
    else:
        print(res)
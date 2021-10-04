q = int(input())
s = [[list(map(int,input().split())) for i in range(2)] for i in range(q)]

def sol(n,knownmov):
    maxmove = 0
    if knownmov.get(n) == None:
        knownmov[n] = 0
    if knownmov[n] > 0:
        return knownmov.get(n)
    else:
        for i in [c for c in lis if c<n and n%c==0]:
            num_move = 1 + (n//i)*sol(i,knownmov)
            if num_move > maxmove:
                maxmove = num_move

        knownmov[n] = maxmove
        return knownmov.get(n)
for k in s:
    lis = k[1]
    pile = k[0][0]
    knownmov = {}
    print(sol(pile,knownmov))
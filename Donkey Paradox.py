n,m= map(int,input().split())
h = []
c = 0
for i in range(2):
    h.append(list(map(int,list(input().split()))))
for y in range(1,n+1):
    for u in range(1,m+1):
        d1 = abs(h[0][0]-y)+abs(h[0][1]-u)
        d2 = abs(h[1][0]-y)+abs(h[1][1]-u)
        if d1 == d2 :
            c += 1
print(c)
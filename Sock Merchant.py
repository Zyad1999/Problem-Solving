n = int(input())
a = list(map(int, input().split()))
a.sort()
c = 0
d = 0
while (c < n-1):
    if(a[c] == a[c+1]):
        d += 1
        c += 2
    else:
        c += 1
print(d)
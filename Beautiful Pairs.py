n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
a.sort()
b.sort()
x = 0
i = 0

for i in a:
    for e in b:
        if e > i:
            break
        if i == e:
            b.remove(e)
            x += 1
            break

if b and len(a) > x:
    print(x+1)
else:
    print(x-1)

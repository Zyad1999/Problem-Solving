n = int(input())
C = []
R = []
r = 0
for i in range(0,n):
    a,b = map(int, input().split())
    R.append(a)
    C.append(b)
for j in R :
    r += j
b = max(C)
C.remove(max(C))
b += max(C)
if (b >= r):
    print("Yes")
else:
    print("No")
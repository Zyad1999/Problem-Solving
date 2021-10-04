n = int(input())
w = int(input())
FFB = [0,1]
if(n % 2 == 0):
    FLB = [n,n+1]
else:
    FLB = [n-1,n]
for i in range(0,(n//2)+1):
    if w in FFB:
        f = i
        break
    else:
        FFB[0] += 2
        FFB[1] += 2
for j in range(0, (n//2)+1):
    if w in FLB :
        l = j
        break
    else:
        FLB[0] -= 2
        FLB[1] -= 2
if (l < f):
    print(l)
else:
    print(f)
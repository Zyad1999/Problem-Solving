x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
if (v1 != v2 and x1 != x2 ):
    n = (x1 - x2) / (v2 - v1)
    if (n > 0 and n % 1 == 0):
        print("YES")
    else:
        print("NO")
elif(v1 == v2 & x1 == x2):
    print("YES")
else:
    print("NO")
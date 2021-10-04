a = list(map(int, input().split()))
l = len(a)
for i in range(0, l-1):
    for j in range(i, l):
        if (j == l-1):
            break
        elif (a[j] == a[j+1]):
            del a[j+1]
        l = len(a)
for i in range(0, len(a)):
    print(a[i], end=" ")
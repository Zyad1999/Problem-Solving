n = int(input())
a = list(map(int, input().split()))
b = a[0]
s = a[0]
l = 0
g = 0
for i in range(1, n):
    if (a[i] > b):
        b = a[i]
        g += 1
    elif (a[i] < s):
        s = a[i]
        l += 1
    else:
        continue
print (g, l)
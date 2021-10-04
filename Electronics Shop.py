n = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
money = n[0]
l1 = n[1]
l2 = n[2]
z = [-1]
for i in range(0, l1):
    for j in range(0, l2):
        s = a[i]+b[j]
        if (s <= money):
            z.append(s)
print(max(z))
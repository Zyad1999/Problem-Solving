n = input()
a = list(map(int, input().split()))
b = a[0]
a.sort()
b = a[len(a)-1]
c = -100
for j in range(0, len(a)):
    if (c < a[j]< b):
        c = a[j]
    else:
        continue
print(c)
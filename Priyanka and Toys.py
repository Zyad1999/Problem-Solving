n = input()
a = list(map(int, input().split()))
x = [0]*10001
c = 0

for i in a:
    x[i] = 1

v = 0
while v < 10001:
    if x[v] == 1:
        c += 1
        v += 4
    v += 1

print(c)

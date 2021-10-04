n = int(input())
a = list(map(int, input().split()))
b = [0, 0, 0, 0, 0]
for i in a :
    if (i == 1):
        b[0] += 1
        continue
    if (i == 2):
        b[1] += 1
        continue
    if (i == 3):
        b[2] += 1
        continue
    if (i == 4):
        b[3] += 1
        continue
    if (i == 5):
        b[4] += 1
        continue
c = b[0]
x = 0
for j in range(0, 5):
    if (b[j] <= c):
        continue
    c = b[j]
    x = j
print(x+1)
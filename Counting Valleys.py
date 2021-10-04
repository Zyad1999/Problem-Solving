n = int(input())
x = input()
HL = 0
valley = 0
for i in range(0, n):
    if (HL == 0):
        if (x[i] == "D"):
            valley += 1
    if (x[i] == "U"):
        HL += 1
    else:
        HL -= 1
print(valley)

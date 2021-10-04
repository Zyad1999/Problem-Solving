n = int(input())
w = list()
m = 0
for i in range(n):
    w.append(sorted(list(input())))
for u in w:
    t = 0
    for k in w:
        if k == u:
            t += 1
    if t > m and t != 1:
        m = t
print(m)
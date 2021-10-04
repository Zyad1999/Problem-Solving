def absloute(x):
    if (x < 0):
        x = x * -1
        return x
    else:
        return x
n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
c1 = 0
for j in range(0, n):
    c1 += a[j][j]
c2 = 0
for k in range(0, n):
    c2 += a[k][n-1]
    n -= 1
c = absloute(c1 - c2)
print (c)
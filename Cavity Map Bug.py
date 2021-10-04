n = int(input())

b = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in map(int, list(input()))]
    b.append(a_t)
a = [x[:] for x in b]

for i in range(1,n-1):
    for j in range(1,n-1):
        if ( b[i][j]> b[i - 1][j] and b[i][j] > b[i][j - 1] and b[i][j] > b[i + 1][j] and b[i][j] > b[i][j + 1]):
            a[i][j] = 'X'

for d in range(0,n):
    for g in range(0,n):
        if (g == n-1):
            print(a[d][g])
        else:
            print(a[d][g], end="")
n = int(input())

a = []
b = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in map(int, list(input()))]
    b.append(a_t)

for i in range(1,n-1):
    for j in range(1,n-1):
        if ( b[i][j]> b[i - 1][j] and b[i][j] > b[i][j - 1] and b[i][j] > b[i + 1][j] and b[i][j] > b[i][j + 1]):
            a.append(i)
            a.append(j)

k = 0
while (k < len(a)):
    b[a[k]][a[k+1]] = 'X'
    k += 2

for d in range(0,n):
    for g in range(0,n):
        if (g == n-1):
            print(b[d][g])
        else:
            print(b[d][g], end="")

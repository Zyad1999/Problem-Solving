import sys

sys.setrecursionlimit(150000)


def largest_matrix_zone(matrix):
    ma = -1
    for i in range(n):
        for j in range(m):
            ma = max(spread(i, j), ma)
    return ma if ma > 0 else -1


def spread(i, j):
    if (matrix[i][j] == 0):
        return 0
    matrix[i][j] = 0

    if (i > 0):
        a = spread(i - 1, j)
    if (j > 0):
        b = spread(i, j - 1)
    if (i < n - 1):
        c = spread(i + 1, j)
    if (j < m - 1):
        d = spread(i, j + 1)

    if (i == 0 or i == n - 1 or j == 0 or j == m - 1 or min([a, b, c, d]) == -1):
        return -1
    return a + b + c + d + 1

n, m = map(int, input().split(' '))
matrix = [0] * n
for i in range(n):
    matrix[i] = list(map(int, input().split(' ')))
answer = largest_matrix_zone(matrix)
print(answer)
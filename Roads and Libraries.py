q = int(input().strip())


def find(a):
    if a != par[a]: par[a] = find(par[a])
    return par[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        par[b] = a
        count[a] += count[b]


for a0 in range(q):
    n, m, x, y = input().strip().split(' ')
    n, m, x, y = [int(n), int(m), int(x), int(y)]

    par = [i for i in range(n + 1)]
    count = [1] * (n + 1)

    for a1 in range(m):
        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]
        union(city_1, city_2)

    ans = 0
    for a1 in range(1, n + 1):
        if a1 == par[a1]: ans += min(x * count[a1], x + y * (count[a1] - 1))

    print(ans)
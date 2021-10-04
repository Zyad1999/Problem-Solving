def solve(A):
    if max(A) <= 0:
        return (max(A), max(A))

    x, y, s, b = 0, 0, 0, 0
    for i, a in enumerate(A):
        if s == 0 and a > 0:
            x = i
        s += a
        if s < 0:
            s = 0

        if s > b:
            b = s
    return (b, sum(a for a in A if a > 0))


T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(_) for _ in input().split()]
    print("%d %d" % solve(A))
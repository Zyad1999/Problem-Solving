def solve(a):
    # Complete this function
    sb = 0
    sa = sum(a)
    for i in a:
        sa -= i
        if sa == sb:
            return "YES"
        sb += i
    return "NO"
T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)
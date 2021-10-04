n, k = map(int, input().split())
a = list(map(int, input().split()))

D_problems = 0
page = 1
j = 0

for CH in range(1, n + 1):

    problems = a[j]

    for c in range(1, problems + 1):

        if c == page:
            D_problems += 1

        if c == problems or c % k == 0:
            page += 1

    j += 1

print(D_problems)
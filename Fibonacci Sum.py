def fibonacci_sum(n):
    fibarray = [1, 1]
    nextfib = 2
    while nextfib <= n:
        nextfib = fibarray[-1] + fibarray[-2]
        if nextfib <= n:
            fibarray.append(nextfib)

    num = 0
    result = []
    for i in reversed(fibarray):
        if num + i <= n:
            result.append(i)

            if num + i == n:
                break
            num += i
    return reversed(result)


n = int(input())
answer = fibonacci_sum(n)
print(' '.join(list(map(str, answer))))
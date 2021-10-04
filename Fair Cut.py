def solve(N, K, A):
    L = N - K
    K, L = min(K,L), max(K,L)

    dp = [[1e32] * (N+1) for i in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(i+1):
            if j > K or i - j > L:
                continue

            li = dp[i][j] + A[i] * ((i - j) - (L - (i - j)))
            if dp[i + 1][j + 1] > li:
                dp[i + 1][j + 1] = li

            lu = dp[i][j] + A[i] * (j - (K - j))
            if dp[i + 1][j] > lu:
                dp[i + 1][j] = lu

    return dp[N][K]

N, K = [int(x) for x in input().split()]
A = sorted([int(x) for x in input().split()])

print(solve(N,K,A))
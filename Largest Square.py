def largest_square(matrix):
    n = len(matrix)
    dp = []
    for i in range(n):
        dp.append([1 for _ in range(n)])
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == 0 or j==0:
                continue
            else:

                if matrix[i][j] == matrix[i-1][j] == matrix[i][j-1] == matrix[i-1][j-1]:
                    dp[i][j] = 1+min(dp[i-1][j] ,dp[i][j-1] ,dp[i-1][j-1])
            ans = max(ans,dp[i][j])
    return ans

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split(' '))))
answer = largest_square(matrix)
print(answer)
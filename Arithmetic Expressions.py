N = int(input())
A = list(map(int, input().split()))
op = ['*'] * (N - 1)
possible = [[None] * 101 for i in range(N)]
possible[0][A[0]] = True
end = N - 1
for i in range(N - 1):
  if possible[i][0]:
    end = i
    break
  for x in range(101):
    if possible[i][x]:
      possible[i + 1][(x + A[i + 1]) % 101] = ('+', x)
      possible[i + 1][(x + 101 - A[i + 1]) % 101] = ('-', x)
      possible[i + 1][(x * A[i + 1]) % 101] = ('*', x)
x = 0
for i in range(end, 0, -1):
  op[i - 1] = possible[i][x][0]
  x = possible[i][x][1]
print(''.join(str(x) for t in zip(A, op) for x in t) + str(A[-1]))
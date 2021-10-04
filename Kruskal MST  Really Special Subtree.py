def kruskal(N, E):
	ans = 0
	sets = {}
	for i in range(1, N+1):
		sets[i] = {i}
	for t in E:
		r, temp, x, y = t
		if y not in sets[x] and x not in sets[y]:
			ans += r
			u = sets[x] | sets[y]
			for j in u:
				sets[j] = u
	return ans

E = []
N, M = map(int, input().split(' '))
for i in range(M):
	x, y, r = map(int, input().split(' '))
	E.append((r, x+y, x, y))
S = int(input())
ans = kruskal(N, sorted(E))
print(ans)
import bisect

def solve():
	prefix = 0
	maxim = 0
	prefixes = []
	N, M = map(int, input().split(' '))
	prefixes.append(0)
	l = map(int, input().split(' '))
	for x in l:
		prefix = (prefix+x)%M
		maxim = max(maxim, prefix)
		j = bisect.bisect_left(prefixes, prefix+1)
		if len(prefixes) != j:
			maxim = max(maxim, prefix - prefixes[j] + M)
		bisect.insort_left(prefixes, prefix)
	return maxim

T = int(input())
for i in range(0, T):
	print(solve())
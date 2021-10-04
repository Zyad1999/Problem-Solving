b = list(map(int, input().split()))
n = b[0]
k = b[1]
q = b[2]
a = list(map(int, input().split()))
for i in range(q):
    x = int(input())
    print (a[(x + n - k) % n])
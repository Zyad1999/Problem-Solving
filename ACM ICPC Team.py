n, m = map(int, input().split())
b = []
a = []
for k in range(0,n):
    a.append(input())
for i in range(0,n):
    for j in range(i+1, n):
        s = bin(int(a[i],2) | (int(a[j],2))).count("1")
        b.append(s)
print (max(b))
print (b.count(max(b)))
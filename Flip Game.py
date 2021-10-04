n,m=list(map(int,input().split()))
a=[]
for i in range(n):
    p=list(map(int,input().split()))
    if p[0]==0:
        p=[1-j for j in p]
    a.append(p)
for i in range(1,m):
    p=[a[j][i] for j in range(n)]
    if p.count(0)>n//2:
        for j in range(n):
            a[j][i]=1-a[j][i]
ans=0
for i in a:
    for j in range(m):
        ans+=pow(2,m-1-j)*i[j]
print(ans)
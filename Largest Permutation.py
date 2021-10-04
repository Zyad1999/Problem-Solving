n,k=[int(i) for i in input().split()]
l=[int(i) for i in input().split()]
if(k>=n):
    k=n-1
i,count=0,0
while(count!=k and i!=n):
    ind=l.index(n-i)
    l[i],l[ind]=l[ind],l[i]
    if(ind!=i):
        count+=1
    i+=1
print(" ".join(map(str,l)))
size=int(input())
li=input().split(' ')
lis=[int(i) for i in li]
lis.sort(reverse=True)
sum=-1
for i in range(0,size,1):
    for j in range(i+1,size,1):
        for k in range(j+1,size,1):
            temp=lis[i]+lis[j]+lis[k]
            if temp>sum and lis[i]<lis[j]+lis[k]:
                sum=temp
                l1,l2,l3=lis[i],lis[j],lis[k]
if sum!=-1:
 print(l3,l2,l1,sep=' ')
else:
 print('-1')
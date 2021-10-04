def justify(v, k):
    i = 0;
    h=[]
    while i<len(v):
        d=[]
        d+=[v[i]]
        sm=len(v[i])
        i+=1
        l=""
        while i<len(v) and sm+len(v[i])+len(d)<=k:
            d+=[v[i]]
            sm+=len(v[i])
            i+=1
        if i==len(v):
            l=" ".join(d)
        else:
            if len(d)==1:l=d[0]+(k-sm)*' '
            else:
                a=((k-sm)//(len(d)-1))+1
                b=((k-sm)%(len(d)-1))
                for j in d[0:b]:
                    l+=j+' '*a
                a-=1
                for j in d[b:-1]:
                    l+=j+' '*a
                l+=d[-1]

        h+=[l]
    return  h


n, k = input().split(' ')
n = int(n)
k = int(k)
v = []
for i in range(n):
    v.append(input())
justified = justify(v, k)
for line in justified:
    print(line)
t=int(input())
while(t>0):
    s=input().split(" ")
    m=s[0]
    n=s[1]
    l1=map(int,input().split(" "))
    l2=map(int,input().split(" "))
    y=[]
    for i in l1:
        y.append([i,0])
    for i in l2:
        y.append([i,1])
    y.sort(reverse=True)
    c=[1,1]
    su=0
    for i in y:
        su=(su+(i[0]*c[i[1]]))%1000000007
        c[1-i[1]]+=1
    print(su)
    t-=1
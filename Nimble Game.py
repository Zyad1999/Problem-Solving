from functools import reduce
test=int(input().strip())
for each in range(test):
    n=int(input().strip())
    ar=[int(i) for i in input().strip().split(" ")]
    arr=[]
    for i in range(1,n):
        if ar[i]%2==1:
            arr.append(i)
    if len(arr)==0:
        print('Second')
        continue
    g=int(reduce(lambda a,b:a^b,arr))
    if g==0:
        print('Second')
    else:
        print('First')
p = int(input())
q = int(input())
x = []


for i in range(p , q+1):

    I = i*i
    l = str(I)
    c = int(l[:int((len(l)/2))])
    c1 = int(l[int((len(l)/2)):])

    if c + c1 == i:
        x.append(i)

if x:
    for k in x:
        print(k, end=" ")
else:
    print("INVALID RANGE")
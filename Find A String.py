a = input()
b = input()
d = len(b)
c = 0
for i in range(0, len(a)):
    if(a[i:d] == b):
        c +=1
    d += 1
print (c)
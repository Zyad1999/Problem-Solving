def DAE (i, b):
    for j in range(0, len(b)):
        if (i % b[j] == 0):
            if(j == len(b)-1):
                return("1")
            else:
                continue
        else:
            return ("0")

def DB (i, c):
    for j in range(0, len(c)):
        if (c[j] % i == 0):
            if (j == len(c)-1):
                return("1")
            else:
                continue
        else:
            return("0")
a = list(map(int, input().split()))
n = a[0]
m = a[1]
b = list(map(int, input().split()))
c = list(map(int, input().split()))
s = 0
for i in range(b[n-1], c[0]+1 ):
    if (DAE(i, b) == "1" and DB(i, c) == "1"):
        s += 1
print (s)
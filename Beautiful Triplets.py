n, d = map(int, input().split())
a = list(map(int, input().split()))
j = 0
for i in a:
    if (i+d in a and i+(2*d) in a):
        j += 1
    elif(i + (2*d) > a[n-1]):
        print(j)
        break
n = int(input())
a = list(set(map(int, input().split())))
x = int(input())
b = list(map(int, input().split()))
a.sort()
o = 0
herRank = len(a)+1
for j in b:
    if (j >= a[len(a) - 1]):
        print(1)
        continue
    for i in range(o, len(a)):
        if(a[i] <= j ):
            herRank -= 1
        else:
            o = i
            break
    print(herRank)
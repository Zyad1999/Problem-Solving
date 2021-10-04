n = int(input())
w = list()
for i in range(n):
    w.append(list([input(),i+1]))
w.sort()
for i in w:
    print(i[1],end=" ")
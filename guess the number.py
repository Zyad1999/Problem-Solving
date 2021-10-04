y = 0
a = list(range(0, 101))
c = 0
while y != 3:
    l = len(a)
    x = a[l//2]
    print(x)
    y = int(input("1-If too big \n""2-If too small \n""3-If right \n"))
    if y == 1:
        a = a[0:l//2]
        c += 1
    elif y == 2:
        a = a[l//2:]
        c += 1
    elif y == 3:
        print("Number of tries:", c)
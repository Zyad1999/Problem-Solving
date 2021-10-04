t = int(input())

for i in range(t):

    b, w = map(int, input().split())
    x, y, z = map(int, input().split())

    if z + y < x:
        units = (b+w)*y
        units += b * z
    elif z + x < y:
        units = (b + w) * x
        units += w * z
    else:
        units = b*x + w*y

    print(units)

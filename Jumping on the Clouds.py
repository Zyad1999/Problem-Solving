def jumpingOnClouds(c):
    x = 0
    co = 0
    while x < len(c)-1:
        if x < len(c)-2 and c[x+2] == 0:
            x += 2
        else:
            x += 1
        co += 1
    return co
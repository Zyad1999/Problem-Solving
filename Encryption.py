msg = input().strip()

from math import ceil, floor, sqrt

def enc(msg):
    sr = sqrt(len(msg))
    row,col = floor(sr),ceil(sr)
    rt = []
    for i in range(col):
        tmp = []
        ind = i
        while ind < len(msg):
            tmp.append(msg[ind])
            ind += col
        tmp = ''.join(tmp)
        rt.append(tmp)
    return ' '.join(rt)

print(enc(msg))
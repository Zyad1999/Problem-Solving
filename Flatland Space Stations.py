#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    x = 0
    c.sort()
    f = 0
    while x< len(c)-1:
        d = c[x+1]-c[x]
        if d>f:
            f = d
        x += 1
    if n-1-c[-1] > (f//2) and n-1-c[-1]>c[0]:
        return n-1-c[-1]
    elif c[0]>(f//2):
        return c[0]
    if f%2 == 0:
        return int(f/2)
    elif f == 1:
        return 0
    else:
        return int((f//2))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()

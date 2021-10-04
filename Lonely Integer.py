#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    b = {}
    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    for i in b:
        if b[i] == 1:
            return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    i = l^r
    re = 1
    while(i):
        re <<= 1
        i >>= 1
    return (re - 1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()

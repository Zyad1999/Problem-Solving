#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):

    d = 9999999999
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
                d = min(d, abs(i - j))

    if d == 9999999999:
        d = -1
    return d
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    s = set()

    for i in range(n):
        s.add(i * a + (n - i - 1) * b)
    s = map(str,list(sorted(s)))
    return( s )

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

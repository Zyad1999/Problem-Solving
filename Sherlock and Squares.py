#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the squares function below.
def squares(a, b):
    c = 0
    for i in range(1, b):
        if i * i in range(a, b + 1):
            c += 1
        elif i * i >= b:
            break
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

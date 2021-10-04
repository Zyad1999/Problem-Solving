#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the lilysHomework function below.
def lilysHomework(a):
    m = {}

    for i in range(len(a)):
        m[a[i]] = i

    sa = sorted(a)
    r = 0

    for i in range(len(a)):
        if a[i] != sa[i]:
            r += 1
            s = m[sa[i]]
            m[a[i]] = m[sa[i]]
            a[i], a[s] = sa[i], a[i]

    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    a = lilysHomework(list(arr))

    d = lilysHomework(list(reversed(arr)))

    result = min(a, d)

    fptr.write(str(result) + '\n')

    fptr.close()

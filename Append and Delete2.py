#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    b = min(len(s), len(t))
    for i in range(len(t)):
        if s[:i] != t[:i]:
            b = i - 1
            break
    d = len(s) - b + len(t) - b
    if (d <= k and d % 2 == k % 2) or len(s) + len(t) < k:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()

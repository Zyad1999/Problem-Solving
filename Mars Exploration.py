#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    d = "SOS"*(len(s)//3)
    c = 0
    i = 0
    while i<len(s):
        if s[i]!=d[i]:
            c += 1
        i += 1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

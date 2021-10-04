#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cost function below.
def cost(B) :
    c0,c1 = 0,0
    for i in range(1,len(B)) :
        c0,c1 = max(c0,c1+B[i-1]-1), max(c0+B[i]-1,c1+abs(B[i]-B[i-1]))
    return max(c0,c1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()

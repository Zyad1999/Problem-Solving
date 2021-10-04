#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    an = []
    while True:
        x = 0
        if len(arr) == 0:
            break
        print(len(arr))
        an.append(len(arr))
        m = min(arr)
        while x < len(arr):
            if arr[x] == m:
                arr.remove(arr[x])
            else:
                arr[x] -= m
                x += 1
    return an
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    b = arr[len(arr)-1]
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i-1]) <= b:
            b = abs(arr[i]-arr[i-1])
    return b


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
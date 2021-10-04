#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(prices):
    p2 = list(prices)
    p2.sort()
    n = 10**10
    for i in range(1,len(prices)):
        if (p2[i]-p2[i-1] < n)  and (prices.index(p2[i]) < prices.index(p2[i-1])):
            n = p2[i]-p2[i-1]
    return(n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
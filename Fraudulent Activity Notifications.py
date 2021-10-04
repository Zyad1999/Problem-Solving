#!/bin/python3

import math
import os
import random
import re
import sys


def search(idx):
    s = 0
    for i in range(0, 200):
        freq = 0
        if i in d:
            freq = d[i]
        s = s + freq
        if s >= idx:
            return i


# Complete the activityNotifications function below.
def activityNotifications(arr, d):
    a = 0
    for i in range(0, n):
        val = arr[i]

        if i >= d:
            med = search(d / 2 + d % 2)

            if d % 2 == 0:
                ret = search(d / 2 + 1)
                if val >= med + ret:
                    a = a + 1
            else:
                if val >= med * 2:
                    a = a + 1

        if val not in d: d[val] = 0
        d[val] = d[val] + 1

        if i >= d:
            prev = arr[i - d]
            d[prev] = d[prev] - 1

    return (a)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    d = {}

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

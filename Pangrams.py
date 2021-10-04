#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    s = s.lower()
    s = list(s)
    a = list("qwertyuiopasdfghjklzxcvbnm")
    for i in a:
        if i in s:
            continue
        else:
            return "not pangram"
    return "pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

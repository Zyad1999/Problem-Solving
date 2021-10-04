#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    c = 0
    current = [r_q, c_q]
    while True:
        current[0] += 1
        if current[0] > n or current in obstacles:
            break
        c += 1
    current = [r_q, c_q]
    while True:
        current[0] -= 1
        if current[0] < 1 or current in obstacles:
            break
        c += 1
    current = [r_q, c_q]
    while True:
        current[1] += 1
        if current[1] > n or current in obstacles:
            break
        c += 1
    current = [r_q, c_q]
    while True:
        current[1] -= 1
        if current[1] < 1 or current in obstacles:
            break
        c += 1
    current = [r_q, c_q]
    while True:
        current[0] += 1
        current[1] += 1
        if current[0] > n or current[1] > n or current in obstacles:
            break
        c += 1
    current = [r_q, c_q]
    while True:
        current[0] -= 1
        current[1] -= 1
        if current[0] < 1 or current[1] < 1 or current in obstacles:
            break
        c += 1
    current = [r_q, c_q]
    while True:
        current[0] += 1
        current[1] -= 1
        if current[0] > n or current[1] < 1 or current in obstacles:
            break
        c += 1
    current = [r_q, c_q]
    while True:
        current[0] -= 1
        current[1] += 1
        if current[0] < 1 or current[1] > n or current in obstacles:
            break
        c += 1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
